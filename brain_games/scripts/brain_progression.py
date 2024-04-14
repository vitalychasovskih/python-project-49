#!/usr/bin/env python3
from brain_games.engine import brain_engine
import brain_games.games.progression


def main():
    """Runs code for the brain-progression command."""
    brain_engine(brain_games.games.progression)


if __name__ == '__main__':
    main()
