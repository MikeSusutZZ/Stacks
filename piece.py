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
            "moveRightOne": self.moveRightOne
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
        return f"{self.id}: ({self.locX}, {self.locY})\n{self.values}\n\n"
