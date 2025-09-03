def run(game) -> None:
    """Generic game runner. Expects game to define:
    - DESCRIPTION: str
    - get_round() -> tuple[str, str]  # (question, correct_answer)
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game.get_round()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
