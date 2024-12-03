# Stacks

Initial notes:

This will serve as a prototype for the board game I had come up with I am currently naming "Stacks", referencing the idea from pokemon of getting "stacks" of stat boosts. This game is a combination of the mind-game and planning aspects of pokemon VGC and the board game style of onitama. I will elaborate on the rules of the game in a further push. This will be focused on the class structure.

## Game State
The game will effectively be split into 2 parts, the cards and the pieces/board. The game state is the connection point between them. Cards will call up to game state, and game state passes that down to the board where the actions will take place. This may be overkill, but having a central point of contact should hopefully make debugging easier. Most of the other classes will be simply holding information rather than taking direct actions, as the game state will handle most of it

Game state will have the board, each players available cards, and each players selected cards.

## Board
The board will hold all of the pieces in a 2D grid of either Piece or None. Pieces will be refered to by their coordinate within the grid.