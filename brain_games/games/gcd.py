# brain_games/games/gcd.py
from math import gcd
from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_round() -> tuple[str, str]:
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    answer = str(gcd(a, b))
    return question, answer
