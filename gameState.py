from board import Board
from card import Card
from piece import Piece
import random

class GameState:
    """
    Holds all of the game data and handles the interaction
    between cards and the pieces on the board
    """
    def __init__(self):
        # Initialize pieces as a dictionary with IDs as keys
        self.pieces = {
            f"p1-{chr(65 + x - 1)}": Piece(x, 1, x == 3, f"p1-{chr(65 + x - 1)}", 1) for x in range(1, 6)
        }
        self.pieces.update({
            f"p2-{chr(65 + x - 1)}": Piece(x, 5, x == 3, f"p2-{chr(65 + x - 1)}", 2) for x in range(1, 6)
        })

        self.p1Cards = []  # Cards for player 1
        self.p2Cards = []  # Cards for player 2
        self.selectedCards = []  # Cards selected for the current round
        self.playerPriority = random.randint(1,2)
        print(f"The player with first priority is {self.playerPriority}")

    def executeRound(self):
        """Go through each card selected, determine the priority
        after stacks, sort them accordingly, and execute each card in order."""
        cards = sorted(self.selectedCards, key=self.getPriority, reverse=True)
        for card in cards:
            self.useCard(card)
        if self.playerPriority == 1:
            self.playerPriority = 2
        else:
            self.playerPriority = 1

    def useCard(self, cardTarPair):
        card, target_id = cardTarPair
        target = self.pieces[target_id]  # Get the piece by its ID
        card.useCard(target, self)

    def getPriority(self, cardPiecePair):
        card, piece_id = cardPiecePair
        piece = self.pieces[piece_id]  # Get the piece by its ID
        priority = card.priority
        priority += piece.values["priority"]
        if piece.player == self.playerPriority:
            priority += 0.5
        return priority

    def printBoard(self, perspective=1):
        """
        Prints the board state in a 5x5 grid with the player's perspective.
        The perspective determines whether Player 1 or Player 2 sees their pieces at the bottom.
        """
        # Initialize an empty 5x5 grid
        grid = [[" " * 7 for _ in range(5)] for _ in range(5)]
        
        # Place pieces on the grid
        for piece in self.pieces.values():
            x, y = piece.locX - 1, piece.locY - 1  # Convert to 0-based index
            grid[y][x] = f"{piece.id:^7}"  # Center-align the piece ID in the cell
        
        # Flip the grid for the respective perspective
        if perspective == 1:
            # Array math is weird, don't mind this, I'll clean it at some point
            grid = grid[::-1]
        else:
            grid = [row[::-1] for row in grid]

        # Print the board with a border
        border = "+" + ("-" * 9 + "+") * 5
        print(border)
        for row in grid:
            row_str = "| " + " | ".join(row) + " |"
            print(row_str)
            print(border)
        print("\n\n")

