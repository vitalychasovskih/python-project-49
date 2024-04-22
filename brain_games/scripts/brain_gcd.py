#!/usr/bin/env python3
from brain_games.engine import start
import brain_games.games.gcd


def main():
    """Run code for the brain-gcd command."""
    start(brain_games.games.gcd)


if __name__ == '__main__':
    main()
