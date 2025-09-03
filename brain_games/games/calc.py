from random import choice, randint
import operator

DESCRIPTION = "What is the result of the expression?"

_OPERATIONS = [
    ("+", operator.add),
    ("-", operator.sub),
    ("*", operator.mul),
]


def get_round() -> tuple[str, str]:
    a = randint(0, 20)
    b = randint(0, 20)
    op_sym, op_func = choice(_OPERATIONS)
    result = op_func(a, b)
    question = f"{a} {op_sym} {b}"  # важно: пробелы по бокам от оператора
    return question, str(result)
