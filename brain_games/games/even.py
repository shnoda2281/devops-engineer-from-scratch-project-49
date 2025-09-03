# brain_games/games/even.py
from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n: int) -> bool:
    return n % 2 == 0


def get_round() -> tuple[str, str]:
    number = randint(1, 100)
    correct = "yes" if is_even(number) else "no"
    return str(number), correct
