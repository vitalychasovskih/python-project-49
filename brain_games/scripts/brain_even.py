#!/usr/bin/env python3
from brain_games.engine import start_game
import brain_games.games.even


def main():
    """Run code for the brain-even command."""
    start_game(brain_games.games.even)


if __name__ == '__main__':
    main()
