import operator
import random

DESCRIPTION = "What is the result of the expression?"

OPS = [
    ("+", operator.add),
    ("-", operator.sub),
    ("*", operator.mul),
]


def get_question_and_answer() -> tuple[str, str]:
    a = random.randrange(1, 21)
    b = random.randrange(1, 21)
    op_sym, op_fn = random.choice(OPS)
    question = f"{a} {op_sym} {b}"
    correct = str(op_fn(a, b))
    return question, correct
