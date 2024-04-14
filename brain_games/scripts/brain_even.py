#!/usr/bin/env python3
from brain_games.engine import brain_engine
import brain_games.games.even


def main():
    """Runs code for the brain-even command."""
    brain_engine(brain_games.games.even)


if __name__ == '__main__':
    main()
