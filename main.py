"""
Main entry point for the Iterated Prisoner's Dilemma project.
Handles user interaction and game/tournament setup.
"""

from game import Game
from tournament import Tournament
from strategies import Strategies
from messages import Messages


class Manager:
    """Manages user interaction and game/tournament flow."""

    def __init__(self) -> None:
        self.player1 = None
        self.player2 = None
        self.game_choice = None

    def welcome(self) -> None:
        """Display welcome message and prompt for start choice."""
        ascii_title = r"""
 ______  __                    ______   ____    ____      
/\__  _\/\ \                  /\__  _\ /\  _`\ /\  _`\    
\/_/\ \/\ \ \___      __      \/_/\ \/ \ \ \L\ \ \ \/\ \  
   \ \ \ \ \  _ `\  /'__`\       \ \ \  \ \ ,__/\ \ \ \ \ 
    \ \ \ \ \ \ \ \/\  __/        \_\ \__\ \ \/  \ \ \_\ \
     \ \_\ \ \_\ \_\ \____\       /\_____\\ \_\   \ \____/
      \/_/  \/_/\/_/\/____/       \/_____/ \/_/    \/___/   ...by EJS
        """
        print(ascii_title)
        self.get_start_choice()

    def get_start_choice(self) -> None:
        """Prompt user to choose between single game or tournament."""
        while True:
            self.game_choice = input(f"\n{Messages.START}").strip().upper()
            if self.game_choice == "G":
                self.player1 = None
                self.player2 = None
                self.get_players()
                break
            elif self.game_choice == "T":
                self.player1 = None
                self.player2 = None
                self.get_round_count()
                break
            else:
                print(Messages.REJECT)

    def get_players(self) -> None:
        """Prompt user to select strategies for both players."""
        while not self.player1:
            player_choice = input("\nChoose Player 1: ").lower().replace(" ", "")
            if player_choice in Strategies.ROSTER:
                self.player1 = Strategies.ROSTER[player_choice]()
                break
            else:
                print(Messages.REJECT, Messages.INVALID_STRATEGY)

        while not self.player2:
            player_choice = input("\nChoose Player 2: ").lower().replace(" ", "")
            if player_choice in Strategies.ROSTER:
                self.player2 = Strategies.ROSTER[player_choice]()
                self.get_round_count()
                break
            else:
                print(Messages.REJECT, Messages.INVALID_STRATEGY)

    def get_round_count(self) -> None:
        """Prompt user to select the number of rounds per game."""
        prompt = (
            "\nChoose number of rounds per game: "
            if self.game_choice == "T"
            else "\nChoose number of rounds: "
        ) # Makes wording clearer
        while True:
            try:
                round_count = int(input(prompt))
                if round_count <= 0:
                    print(Messages.REJECT, Messages.NOT_A_POS_INT)
                    continue
                break
            except ValueError:
                print(Messages.REJECT, Messages.NOT_AN_INT)

        if self.game_choice == "G":
            g = Game(self.player1, self.player2, round_count)
            g.play_game()
            print(g)
            g.print_rounds()
            self.game_choice = None # Redundant for now
        else:
            t = Tournament(round_count)
            t.play_tournament()
            print(t)
            self.game_choice = None



if __name__ == "__main__":
    manager = Manager()
    manager.welcome()
