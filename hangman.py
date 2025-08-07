import random

words = ["love", "marangi", "watermelon", "pineapple", "mango", "cashewnut", "groundnut"]

hangman_mockup = {
    0: (
        "   ",
        "   ",
        "   "

    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}

def display_man(wrong_guesses):
    for man in hangman_mockup[wrong_guesses]:
        print(man)
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("".join(answer))

def main():
    answer = random.choice(words)
    hint = ["-"] * len(answer)
    wrong_guesses = 0
    is_running = True
    guessed_letters = set()
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter your guess ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "-" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("YOU WIN!!🥳🥳")
            is_running = False
        elif wrong_guesses >= len(hangman_mockup) - 1:
            display_man(wrong_guesses)
            display_hint(hint)
            print("YOU LOSE!😢😢")
            is_running = False

if __name__ == "__main__":
    main()