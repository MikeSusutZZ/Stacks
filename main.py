from gameState import GameState
from piece import Piece
from card import Card

gameState = GameState()

# Create pieces for both players

gameState.printBoard()

# gameState.executeRound()
# gameState.printBoard()


# gameState.selectedCards.append((Card("approach"), "p1-C"))
# gameState.selectedCards.append((Card("approach"), "p2-C"))
# gameState.selectedCards.append((Card("strafe left"), "p2-C"))
# gameState.selectedCards.append((Card("strafe right"), "p1-C"))
gameState.p1Cards.append(Card("advance"))
gameState.p1Cards.append(Card("test"))
while True:
    gameState.executeRound()
    gameState.printBoard()

gameState.printBoard(2)


# # Move Player 1 (normal perspective)
# piece1.takeAction("addNegativeAttackStack", gameState)
# piece1.takeAction("moveUpOne", gameState)  # Moves to (0, 1)
# piece1.takeAction("moveRightOne", gameState)  # Moves to (1, 1)

# # Move Player 2 (inverted perspective)
# piece2.takeAction("moveUpOne", gameState)  # Moves to (5, 4)
# piece2.takeAction("moveLeftOne", gameState)  # Moves to (4, 4)

