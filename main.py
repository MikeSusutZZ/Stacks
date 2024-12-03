from gameState import GameState
from piece import Piece
from card import Card

gameState = GameState()

# Create pieces for both players
piece1 = Piece(1, 1, True, "P1", 1)
piece2 = Piece(5, 5, True, "P2", 2)

gameState.pieces.extend([piece1, piece2])

# Move Player 1 (normal perspective)
piece1.takeAction("addAttackStack", gameState)
piece1.takeAction("moveUpOne", gameState)  # Moves to (0, 1)
piece1.takeAction("moveRightOne", gameState)  # Moves to (1, 1)

# Move Player 2 (inverted perspective)
piece2.takeAction("moveUpOne", gameState)  # Moves to (5, 4)
piece2.takeAction("moveLeftOne", gameState)  # Moves to (4, 4)

