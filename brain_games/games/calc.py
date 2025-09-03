# brain_games/games/calc.py
from random import choice, randint

DESCRIPTION = "What is the result of the expression?"


def _compute(a: int, op: str, b: int) -> int:
    # можно через match/case (Python 3.10+)
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case _:
            raise ValueError(f"Unsupported operator: {op}")


def get_round() -> tuple[str, str]:
    a = randint(1, 50)
    b = randint(1, 50)
    op = choice(["+", "-", "*"])
    question = f"{a} {op} {b}"
    answer = str(_compute(a, op, b))
    return question, answer
