# brain_games/games/prime.py
from math import isqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    # проверяем только нечётные делители
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


def get_round() -> tuple[str, str]:
    number = randint(1, 200)  # диапазон можно менять
    correct = "yes" if _is_prime(number) else "no"
    return str(number), correct
