"""
Game logic for the Iterated Prisoner's Dilemma.
Handles a single game between two strategies.
"""

from context import Context
from payoff import Payoff
from messages import Messages


class Game:
    """Manages a single game between two strategies."""

    def __init__(self, player1, player2, round_count: int) -> None:
        self.player1 = player1
        self.player2 = player2
        self.round_count = round_count
        self.round_number = 1
        self.history = []
        self.scores = {"Player 1": 0, "Player 2": 0}
        self.player_names = {
            "Player 1": self.player1.name,
            "Player 2": self.player2.name,
        }
        self.max_name_len = max_name_len = max(len(name) for name in self.player_names.values())


    def __str__(self) -> str:
        """Return game results as a formatted string."""
        lines = ["\n===== Game Results =====\n"]

        if self.scores["Player 1"] != self.scores["Player 2"]:
            sorted_scores = sorted(
                self.scores.items(), key=lambda item: item[1], reverse=True
            )
            for slot, score in sorted_scores:
                player_name = self.player_names[slot]
                lines.append(f"{player_name:<{self.max_name_len}} : {score}")

            winner_slot = max(self.scores, key=self.scores.get)            
            lines.append(f"\nWINNER: {self.player_names[winner_slot]}")

        else:
            lines.append(f"{self.player_names["Player 1"]:<{self.max_name_len}} : {self.scores["Player 1"]}")
            lines.append(f"{self.player_names["Player 2"]:<{self.max_name_len}} : {self.scores["Player 2"]}")
            lines.append("\nTIE GAME")

        return "\n".join(lines)

    def play_round(self) -> None:
        """Play a single round and update history and scores."""
        context1 = Context(
            [h[0] for h in self.history],
            [h[1] for h in self.history],
            self.round_number,
            self.scores["Player 1"],
        )
        context2 = Context(
            [h[1] for h in self.history],
            [h[0] for h in self.history],
            self.round_number,
            self.scores["Player 2"],
        )
        action1 = self.player1.choose_action(context1)
        action2 = self.player2.choose_action(context2)
        self.history.append((action1, action2))

        score1, score2 = Payoff.payoffs[(action1, action2)]
        self.scores["Player 1"] += score1
        self.scores["Player 2"] += score2

        self.round_number += 1

    def play_game(self, single_game=True) -> dict:
        """Play the full game and optionally print results."""
        while self.round_number <= self.round_count:
            self.play_round()
        
        if not single_game:
            return self.scores
        
    def print_rounds(self) -> None:
        """Print each round of a game"""
        while True:
            want_see_rounds = input("\nWould you like to see each round of the game (Y/N): ").strip().upper()

            if want_see_rounds == "Y":
                for i, r in enumerate(self.history, start=1):
                    print("")
                    print("-" * 25)
                    print(f"\nRound {i}:")
                    print(f"{self.player1.name:<{self.max_name_len}} : {r[0]}")
                    print(f"{self.player2.name:<{self.max_name_len}} : {r[1]}")
                print("\n" + "-" * 25)
                break
            elif want_see_rounds == "N":
                break
            else:
                print(Messages.REJECT, Messages.Y_OR_N)
                continue