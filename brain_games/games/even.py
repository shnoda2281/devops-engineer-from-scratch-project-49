import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n: int) -> bool:
    return n % 2 == 0


def get_question_and_answer() -> tuple[str, str]:
    number = random.randrange(1, 101)
    correct = "yes" if is_even(number) else "no"
    return str(number), correct
