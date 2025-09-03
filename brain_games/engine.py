# brain_games/engine.py

def run_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
