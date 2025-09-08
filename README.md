# Iterated Prisoner's Dilemma Project

This project simulates the Iterated Prisoner's Dilemma (IPD) with a variety of strategies. You can run single games or round-robin tournaments between all strategies.

*Inspired by Professor Robert Axelrod's Iterated Prisoner's Dilemma Tournaments (1979–1980).*

Learn more about the Prisoner's Dilemma on [Wikipedia](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma).

## Why I Built This
> I created this project to deepen my understanding of game theory, strategy design, and Python software architecture. The Iterated Prisoner's Dilemma is a classic problem that offers rich opportunities for exploring algorithmic decision-making and most notably (and excitingly, to me), emergent behavior!

## What I Learned
> Through this project, I learned about designing extensible systems, implementing and testing a variety of algorithms, and managing user interaction in a command-line application. I also gained experience with Python's OOP features and best practices for code organization.

## Features
- Play a single game between any two strategies
- Run a tournament where all strategies play each other
- Choose the number of rounds in a game
- Extensible: add your own strategies easily

## How to Run
1. **Install Python 3** (if not already installed)
2. Open a terminal in this project directory
3. Run:
   ```
   python3 main.py
   ```
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

## Files
- `main.py`: Main entry point (CLI), handles user interaction and game/tournament setup.
- `game.py`: Game logic for a single match between two strategies.
- `tournament.py`: Tournament logic for round-robin play between all strategies.
- `strategies.py`: All strategy definitions, base class, and registration system.
- `context.py`: Context object passed to strategies, containing game state information.
- `payoff.py`: Defines the payoff matrix and values for the game.
- `messages.py`: Centralized static messages for user prompts and errors.
- `test_strategies.py`: Unit tests for strategies and game logic.
- `NOTES.md`: Personal ramblings.

## License
MIT License
