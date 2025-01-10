from stack import Stack

class Piece:
    def __init__(self, startingCoordX, startingCoordY, master, id, player) -> None:
        self.id = id
        self.player = player
        self.locX = startingCoordX
        self.locY = startingCoordY
        self.stacks = []
        self.master = master
        self.values = {"attack": 0, "defence": 0, "priority": 0}
        self.actions = {
            "addAttackStack": lambda gameState: self.addStack("attack", 1),
            "addDefenceStack": lambda gameState: self.addStack("defence", 1),
            "addPriorityStack": lambda gameState: self.addStack("priority", 1),
            "addNegativeAttackStack": lambda gameState: self.addStack("attack", -1),
            "addNegativeDefenceStack": lambda gameState: self.addStack("defence", -1),
            "addNegativePriorityStack": lambda gameState: self.addStack("priority", -1),
            "moveUpOne": self.moveUpOne,
            "moveDownOne": self.moveDownOne,
            "moveLeftOne": self.moveLeftOne,
            "moveRightOne": self.moveRightOne,
            "addNegativeAttackStackToOpp": lambda gameState: self.addNegativeStackToOpp("attack", gameState),
            "addNegativeDefenceStackToOpp": lambda gameState: self.addNegativeStackToOpp("defence", gameState),
            "addNegativePriorityStackToOpp": lambda gameState: self.addNegativeStackToOpp("priority", gameState),
        }
        self.updateValues()

    def handleCollision(self, gameState, targetX, targetY):
        """Check for collision at the target location."""
        for piece in gameState.pieces.values():
            if piece is self:
                continue  # Skip checking against itself
            if piece.locX == targetX and piece.locY == targetY:
                if piece.player != self.player:
                    # Enemy collision: Attack vs. Defence comparison
                    if self.values["attack"] >= piece.values["defence"]:
                        print(f"{self.id} captured {piece.id}")
                        self.looseStack()
                        gameState.pieces.remove(piece)  # Remove captured piece
                        return True
                    else:
                        # Bounce off the stronger defender
                        piece.looseStack()
                        print(f"{self.id} bounced off {piece.id}")
                        return False
                else:
                    # Friendly collision
                    print(f"{self.id} ran into friendly piece {piece.id}")
                    return False
        return True  # No collision; movement allowed

    def adjust_player_dir(self, x):
        """Adjust movement based on player's perspective."""
        if self.player == 2:
            # Invert the movement for Player 2
            x = -x
        return x

    def looseStack(self):
        if self.stacks:
            self.stacks.pop()
            self.updateValues()
        else:
            print(f"{self.id} has no stacks to lose.")

    def addStack(self, stackType, amt):
        if len(self.stacks) < 3:
            print(f"Adding a {stackType} stack with amount {amt}")
            self.stacks.append(Stack(stackType, amt))
            self.updateValues()
        else:
            print(f"{self.id} already has maximum stacks.")

    def moveUpOne(self, gameState):
        targetX, targetY = self.locX, self.locY + self.adjust_player_dir(1)
        if 0 <= targetY <= 5 and self.handleCollision(gameState, targetX, targetY):
            self.locY = targetY
            print(f"{self.id} moved to ({self.locX}, {self.locY})")
        else:
            print(f"{self.id} didn't move")

    def moveDownOne(self, gameState):
        targetX, targetY = self.locX, self.locY - self.adjust_player_dir(1)
        if 0 <= targetY <= 5 and self.handleCollision(gameState, targetX, targetY):
            self.locY = targetY
            print(f"{self.id} moved to ({self.locX}, {self.locY})")
        else:
            print(f"{self.id} didn't move")

    def moveLeftOne(self, gameState):
        targetX, targetY = self.locX - self.adjust_player_dir(1), self.locY
        if 0 <= targetX <= 5 and self.handleCollision(gameState, targetX, targetY):
            self.locX = targetX
            print(f"{self.id} moved to ({self.locX}, {self.locY})")
        else:
            print(f"{self.id} didn't move")

    def moveRightOne(self, gameState):
        targetX, targetY = self.locX + self.adjust_player_dir(1), self.locY
        if 0 <= targetX <= 5 and self.handleCollision(gameState, targetX, targetY):
            self.locX = targetX
            print(f"{self.id} moved to ({self.locX}, {self.locY})")
        else:
            print(f"{self.id} didn't move")

    def addNegativeStackToOpp(self, stackType, gameState):
        """Applies a negative stack to an opponent within one space of the piece."""
        nearby_pieces = [
            piece for piece in gameState.pieces.values()
            if piece.player != self.player and
            abs(piece.locX - self.locX) <= 1 and
            abs(piece.locY - self.locY) <= 1
        ]
        if not nearby_pieces:
            print("No valid targets within range.")
            return

        print("Select a target to apply the negative stack:")
        for i, piece in enumerate(nearby_pieces, start=1):
            print(f"{i}: {piece.id} at ({piece.locX}, {piece.locY})")

        while True:
            try:
                choice = int(input("Enter the number of the target (or 0 to cancel): "))
                if choice == 0:
                    print("Action canceled.")
                    return
                if 1 <= choice <= len(nearby_pieces):
                    target = nearby_pieces[choice - 1]
                    target.addStack(stackType, -1)
                    print(f"Applied a negative {stackType} stack to {target.id}.")
                    return
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def takeAction(self, name, gameState):
        # Look for the method in the dictionary and call it
        if name in self.actions:
            self.actions[name](gameState)
        else:
            print(f"Action {name} not found.")

    def updateValues(self):
        # Reset values to defaults
        for value in self.values:
            self.values[value] = 0
        if self.master:
            self.values["attack"] = 1
            self.values["defence"] = 1
        for stack in self.stacks:
            self.values[stack.type] += stack.amt

    def __str__(self) -> str:
        # Format stacks as a string with their type and amount
        stacks_str = ", ".join([f"{stack.type}({stack.amt})" for stack in self.stacks]) if self.stacks else "No stacks"
        
        # Format values as a string
        values_str = ", ".join([f"{key}: {value}" for key, value in self.values.items()])
        
        return (f"Piece ID: {self.id}\n"
                f"Stacks: {stacks_str}\n"
                f"Values: {values_str}\n")

