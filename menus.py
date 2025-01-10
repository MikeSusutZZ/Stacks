import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Menu:
    """
    Handles the card and targeting selection menu for players.
    """

    @staticmethod
    def getCardSelection(player_cards, player_pieces, max_cards=3):
        """
        Allows a player to select cards for their pieces.

        Args:
            player_cards (list): List of available cards for the player.
            player_pieces (dict): Dictionary of player's pieces.
            max_cards (int): Maximum number of cards a player can select.

        Returns:
            list: A list of selected card-target pairs [(card, target_id), ...].
        """
        selected_cards = []
        used_cards = set()

        print("\nAvailable Cards:")
        for idx, card in enumerate(player_cards, start=1):
            print(f"{idx}: {card.name} (Priority: {card.priority})")
        print("0: Skip")

        for piece_id, piece in player_pieces.items():
            if len(selected_cards) >= max_cards:
                print("You have reached the maximum number of selected cards.")
                break

            print(f"\nSelecting a card for piece: {piece_id} (Location: ({piece.locX}, {piece.locY}))")
            while True:
                try:
                    choice = int(input("Choose a card number or 0 to skip: "))
                    if choice == 0:
                        print(f"Skipped piece {piece_id}.")
                        break

                    if choice < 0 or choice > len(player_cards):
                        print("Invalid choice. Please choose a valid card number.")
                        continue

                    if choice in used_cards:
                        print("This card has already been used. Choose a different card.")
                        continue

                    selected_cards.append((player_cards[choice - 1], piece_id))
                    used_cards.add(choice)
                    print(f"Assigned card '{player_cards[choice - 1].name}' to piece {piece_id}.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        return selected_cards

    @staticmethod
    def assignCards(game_state):
        """
        Facilitates card selection for both players.

        Args:
            game_state (GameState): The current game state.

        Updates:
            game_state.selectedCards: List of card-target pairs for the current round.
        """
        game_state.printBoard()
        print("Player 1, it is your turn to assign cards.")
        p1_selected = Menu.getCardSelection(game_state.p1Cards, 
                                            {k: v for k, v in game_state.pieces.items() if v.player == 1})
        clear_console()
        
        game_state.printBoard(2)
        print("Player 2, it is your turn to assign cards.")
        p2_selected = Menu.getCardSelection(game_state.p2Cards, 
                                            {k: v for k, v in game_state.pieces.items() if v.player == 2})

        game_state.selectedCards = p1_selected + p2_selected
