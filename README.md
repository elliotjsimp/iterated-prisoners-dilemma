# Iterated Prisoner's Dilemma Project

This project simulates the Iterated Prisoner's Dilemma (IPD) with a variety of strategies. You can run single games or round-robin tournaments between all strategies. Want to add custom strategies of your own? See below.

*Inspired by Professor Robert Axelrod's Iterated Prisoner's Dilemma Tournaments (1979–1980).*

Learn more about the Prisoner's Dilemma on [Wikipedia](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma).

## Features
- Play a single game between any two strategies
- Run a tournament where all strategies play each other
- Choose the number of rounds in a game
- Extensible: add your own strategies easily

4. Follow the prompts to select game mode, strategies, and number of rounds

## Strategies Included
- AlwaysCooperate
- AlwaysDefect
- TitForTat
- SuspiciousTitForTat
- GenerousTitForTat
- TitForTwoTats
- TwoTatsForTit
- ImperfectTitForTat
- WinStayLoseShift
- Trigger
- Random

Descriptions of each strategy’s behaviour can be found in `strategies.py`, but the behaviour is best understood through play.

## How to Add a New Strategy
1. Open `strategies.py`.
2. Subclass the `Strategy` base class and implement the `choose_action` method.
3. Register your new class with the `Strategies` roster using `Strategies.register`, giving it a unique key.
> Note: The registration line must be **outside** the class definition.

Example:
```python
class MyStrategy(Strategy):
    def choose_action(self, context: Context) -> str:
        # Your logic here
        return "C"  # or "D"

# Register the strategy so it can be used
Strategies.register("mystrategy", MyStrategy)
```

## License
MIT License
