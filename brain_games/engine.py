ROUNDS_COUNT = 3  # количество раундов вынесено в константу


def run(game) -> None:
    """Generic game runner.
    Требуется у game:
      - DESCRIPTION: str
      - get_question_and_answer() -> (question, correct_answer)
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()

        if answer != str(correct_answer):
            msg = (
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(msg)
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {name}!")
