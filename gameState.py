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
        cards = sorted(self.selectedCards, key=self.getPriority, reverse=True)
        for card in cards:
            self.useCard(card)
        pass

    def useCard(self, cardTarPair):
        card, target = cardTarPair
        card.useCard(target, self)

    def getPriority(self, cardPiecePair):
        card, piece = cardPiecePair
        priority = card.priority
        priority += piece.values["priority"]
        return priority
        