"""
Strategy definitions for the Iterated Prisoner's Dilemma.
To add a new strategy, subclass Strategy and add it to Strategies.ROSTER.
"""

from payoff import Payoff
from context import Context
import random


class Strategy:
    """Base class for all strategies."""

    def __init__(self) -> None:
        self.name = self.__class__.__name__

    def choose_action(self, context: Context) -> str:
        """Return 'C' (cooperate) or 'D' (defect) given the context."""
        raise NotImplementedError


class Strategies:
    """Holds the roster of available strategies."""

    ROSTER = {}
   
    @classmethod
    def register(cls, id: str, strategy_cls: type[Strategy]) -> None:
        """Register a new strategy class by a unique id string. Note: class name is used as display name in CLI."""
        if id in cls.ROSTER:
            raise ValueError(f"Strategy '{id}' already exists in the roster.")
        cls.ROSTER[id] = strategy_cls


class AlwaysCooperate(Strategy):
    """Always cooperates."""

    def choose_action(self, context: Context) -> str:
        return "C"


class AlwaysDefect(Strategy):
    """Always defects."""

    def choose_action(self, context: Context) -> str:
        return "D"


class TitForTat(Strategy):
    """Cooperates first, then mimics opponent's last move."""

    def choose_action(self, context: Context) -> str:
        if not context.opponent_history:
            return "C"
        return context.opponent_history[-1]


class SuspiciousTitForTat(Strategy):
    """Defects first, then mimics opponent's last move."""

    def choose_action(self, context: Context) -> str:
        if not context.opponent_history:
            return "D"
        return context.opponent_history[-1]


class GenerousTitForTat(Strategy):
    """Like TitForTat, but sometimes forgives a defection."""

    def choose_action(self, context: Context) -> str:
        if not context.opponent_history or context.opponent_history[-1] == "C":
            return "C"
        if self.coop_probability() > random.random():
            return "C"
        return "D"

    def coop_probability(self) -> float:
        T, R, P, S = Payoff.T, Payoff.R, Payoff.P, Payoff.S
        return min(1 - (T - R) / (R - S), (R - P) / (T - P))


class TitForTwoTats(Strategy):
    """Defects only if opponent defected twice in a row."""

    def choose_action(self, context: Context) -> str:
        if context.opponent_history[-2:] == ["D", "D"]:
            return "D"
        return "C"


class TwoTatsForTit(Strategy):
    """Defects twice after being defected against once, otherwise cooperates."""

    def __init__(self) -> None:
        super().__init__()
        self.defects_left = 0

    def choose_action(self, context: Context) -> str:
        if self.defects_left > 0:
            self.defects_left -= 1
            return "D"
        if context.opponent_history[-1:] == ["D"]:
            self.defects_left = 1
            return "D"
        return "C"


class ImperfectTitForTat(Strategy):
    """Imitates opponent's last move with high (but less than one) probability."""

    def choose_action(self, context: Context) -> str:
        coop_probability = 0.99 # a
        if not context.opponent_history:
            return "C"
        if context.opponent_history[-1] == "C":
            return "C" if coop_probability > random.random() else "D"
        else:
            return "D" if coop_probability > random.random() else "C"
        
class Trigger(Strategy):
    """Cooperates until opponent defects, then always defects."""

    def __init__(self) -> None:
        super().__init__()
        self.opponent_defected = False

    def choose_action(self, context: Context) -> str:
        if context.opponent_history and context.opponent_history[-1] == "D":
            self.opponent_defected = True
        return "D" if self.opponent_defected else "C"


class WinStayLoseShift(Strategy):
    """If last move gave good return, repeat, otherwise change (Pavlov)."""
    def choose_action(self, context: Context) -> str:
        if not context.my_history:
            return "C"
        
        my_last = context.my_history[-1]
        opponent_last = context.opponent_history[-1]
        
        # Calculate last round’s payoff
        if my_last == "C" and opponent_last == "C":  # Reward
            return "C"   # stay
        if my_last == "D" and opponent_last == "C":  # Temptation
            return "D"   # stay
        if my_last == "D" and opponent_last == "D":  # Punishment
            return "C"   # shift
        if my_last == "C" and opponent_last == "D":  # Sucker
            return "D"   # shift

class Random(Strategy):
    """Randomly cooperates or defects."""

    def choose_action(self, context: Context) -> str:
        return random.choice(["C", "D"])
    

# --- Registration ---

Strategies.register("alwayscooperate", AlwaysCooperate)
Strategies.register("alwaysdefect", AlwaysDefect)
Strategies.register("titfortat", TitForTat)
Strategies.register("suspicioustitfortat", SuspiciousTitForTat)
Strategies.register("generoustitfortat", GenerousTitForTat)
Strategies.register("titfortwotats", TitForTwoTats)
Strategies.register("twotatsfortit", TwoTatsForTit)
Strategies.register("imperfecttitfortat", ImperfectTitForTat)
Strategies.register("trigger", Trigger)
Strategies.register("winstayloseshift", WinStayLoseShift)
Strategies.register("random", Random)
