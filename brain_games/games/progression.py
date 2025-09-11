import random

DESCRIPTION = 'What number is missing in the progression?'

PROG_LEN = 10


def get_question_and_answer() -> tuple[str, str]:
    start = random.randrange(1, 11)
    step = random.randrange(2, 6)
    hidden_idx = random.randrange(PROG_LEN)

    progression = [start + i * step for i in range(PROG_LEN)]
    correct = str(progression[hidden_idx])
    progression[hidden_idx] = ".."
    question = " ".join(map(str, progression))
    return question, correct
