# brain_games/games/progression.py
from random import choice, randint

DESCRIPTION = "What number is missing in the progression?"


def _build_progression(start: int, step: int, length: int) -> list[int]:
    # a_i = start + i * step
    return [start + i * step for i in range(length)]


def get_round() -> tuple[str, str]:
    # Длина 5..10 (рекомендуем 10, но можно варьировать)
    length = choice([10, 9, 8, 7, 6, 5])
    start = randint(1, 20)
    step = randint(1, 10)

    prog = _build_progression(start, step, length)
    hidden_idx = randint(0, length - 1)
    correct = str(prog[hidden_idx])

    shown = [str(x) for i, x in enumerate(prog)]
    shown[hidden_idx] = ".."
    question = " ".join(shown)

    return question, correct
