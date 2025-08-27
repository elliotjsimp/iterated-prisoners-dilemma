"""
Tournament logic for the Iterated Prisoner's Dilemma.
Runs a round-robin tournament between all strategies.
"""

from strategies import Strategies
from game import Game


class Tournament:
    """Manages a round-robin tournament between all strategies."""

    def __init__(self, round_count: int):
        self.round_count = round_count  # per-game round count, not total count of games
        self.tournament_scores = {key: 0 for key in Strategies.ROSTER}

    def __str__(self) -> str:
        """Returns tournament results as a formatted string, sorted by score."""
        lines = ["\n===== Tournament Results =====\n"]
        sorted_scores = sorted(
            self.tournament_scores.items(), key=lambda item: item[1], reverse=True
        )
        max_name_len = max(
            len(name)
            for name in self.tournament_scores
        )
        for name, score in sorted_scores:
            lines.append(f"{Strategies.ROSTER[name].__name__:<{max_name_len}} : {score}")

        winner_key, winner_score = sorted_scores[0]
        winner_name = Strategies.ROSTER[winner_key].__name__
        lines.append(f"\nWINNER: {winner_name} with {winner_score} points!\n")
        return "\n".join(lines)

    def play_tournament(self) -> None:
        """Play a round-robin tournament (with self-play) and print results."""
        for strategy1 in Strategies.ROSTER:
            for strategy2 in Strategies.ROSTER:
                g = Game(
                    Strategies.ROSTER[strategy1](),
                    Strategies.ROSTER[strategy2](),
                    self.round_count,
                )
                game_scores = g.play_game(single_game=False)
                self.tournament_scores[strategy1] += game_scores["Player 1"]
                self.tournament_scores[strategy2] += game_scores["Player 2"]