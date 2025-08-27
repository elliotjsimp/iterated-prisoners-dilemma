import unittest
from strategies import Strategies, AlwaysCooperate, AlwaysDefect
from game import Game
from context import Context


class TestStrategies(unittest.TestCase): # TODO: add more tests
    def test_always_cooperate_vs_always_defect(self):
        coop = AlwaysCooperate()
        defect = AlwaysDefect()
        game = Game(coop, defect, 5)
        scores = game.play_game(verbose=False)
        self.assertEqual(scores["Player 1"], 0)  # AlwaysCooperate gets sucker's payoff every round
        self.assertEqual(scores["Player 2"], 25)  # AlwaysDefect gets temptation every round

    def test_strategy_instantiation_and_action(self):
        dummy_context = Context([], [], 1, 0)
        for name, cls in Strategies.ROSTER.items():
            strat = cls()
            action = strat.choose_action(dummy_context)
            self.assertIn(action, ["C", "D"], f"{name} did not return a valid action")


if __name__ == "__main__":
    unittest.main()
