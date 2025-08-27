"""
Payoff matrix for the Iterated Prisoner's Dilemma.
"""


class Payoff:
    """Defines the payoff values and matrix for the game."""

    T: int = 5  # Temptation to defect
    R: int = 3  # Reward for mutual cooperation
    P: int = 1  # Punishment for mutual defection
    S: int = 0  # Sucker's payoff
    payoffs = {
        ("C", "C"): (R, R),
        ("C", "D"): (S, T),
        ("D", "C"): (T, S),
        ("D", "D"): (P, P),
    }
