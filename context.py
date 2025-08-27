"""
Context object passed to strategies, containing game state information.
"""


class Context:
    """Holds the history, round number, and score for a player in a game."""

    def __init__(
        self, my_history: list, opponent_history: list, round_number: int, score: int
    ) -> None:
        self.my_history = my_history
        self.opponent_history = opponent_history
        self.round_number = round_number
        self.score = score
