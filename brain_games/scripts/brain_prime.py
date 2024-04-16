#!/usr/bin/env python3
from brain_games.engine import start_game
import brain_games.games.prime


def main():
    """Run code for the brain-prime command."""
    start_game(brain_games.games.prime)


if __name__ == '__main__':
    main()
