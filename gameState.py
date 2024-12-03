from board import Board
from card import Card
from piece import Piece

class GameState:
    """
    Holds all of the game data and handles the interaction
    between cards and the pieces on the board
    """
    def __init__(self):
        self.pieces = [
            Piece(1, 1, False, "p1-A", 1),
        ]
        self.p1Cards = []
        self.p2Cards = []
        self.selectedCards = []

    def executeRound(self):
        """Go through each card selected, determine the priority
        after stacks, sort them accordingly, and execute each card in order"""
        pass

    def useCard(self, target, card):
        for action in card.actions:
            action.execute(target)
        