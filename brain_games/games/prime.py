from math import isqrt
from random import randrange

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def get_question_and_answer() -> tuple[str, str]:
    number = randrange(1, 201)
    correct = "yes" if is_prime(number) else "no"
    return str(number), correct
