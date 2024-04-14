#!/usr/bin/env python3
from brain_games.engine import brain_engine
import brain_games.games.calc


def main():
    """Runs code for the brain-calc command."""
    brain_engine(brain_games.games.calc)


if __name__ == '__main__':
    main()
