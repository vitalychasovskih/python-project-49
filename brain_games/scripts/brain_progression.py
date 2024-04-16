#!/usr/bin/env python3
from brain_games.engine import start_game
import brain_games.games.progression


def main():
    """Run code for the brain-progression command."""
    start_game(brain_games.games.progression)


if __name__ == '__main__':
    main()
