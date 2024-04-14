#!/usr/bin/env python3
from brain_games.engine import brain_engine
import brain_games.games.gcd


def main():
    """Runs code for the brain-gcd command."""
    brain_engine(brain_games.games.gcd)


if __name__ == '__main__':
    main()
