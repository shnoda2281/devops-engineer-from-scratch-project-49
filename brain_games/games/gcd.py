import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def get_question_and_answer() -> tuple[str, str]:
    a = random.randrange(1, 101)
    b = random.randrange(1, 101)
    question = f"{a} {b}"
    correct = str(math.gcd(a, b))
    return question, correct
