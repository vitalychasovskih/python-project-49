#!/usr/bin/env python3
from brain_games.engine import start
import brain_games.games.calc


def main():
    """Run code for the brain-calc command."""
    start(brain_games.games.calc)


if __name__ == '__main__':
    main()
