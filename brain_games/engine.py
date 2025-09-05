ROUNDS_COUNT = 3  # количество раундов вынесено в константу


def run(game) -> None:
    """Generic game runner.
    Игра должна определять:
      - DESCRIPTION: str
      - get_question_and_answer() -> (question, correct_answer)  # новый стиль
        ИЛИ
      - get_round() -> (question, correct_answer)                # старый стиль
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    # Определяем, какую функцию вызова раунда использовать
    if hasattr(game, "get_question_and_answer"):
        get_q_and_a = game.get_question_and_answer
    elif hasattr(game, "get_round"):
        get_q_and_a = game.get_round
    else:
        raise AttributeError(
            "Game module must define get_question_and_answer() or get_round()."
        )

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_q_and_a()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()

        if answer != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
    else:  # выполнится, если цикл прошёл без break
        print(f"Congratulations, {name}!")
