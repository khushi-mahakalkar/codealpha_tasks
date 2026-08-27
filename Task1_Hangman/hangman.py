import random

print("=" * 50)
print("                  CODE DETECTIVE")
print("=" * 50)
print("               Crack the Secret Word!")
print("=" * 50)

words = {
    "python": [
        "A programming language",
        "It is known for its simple syntax",
        "Its name is related to a type of snake"
    ],
    "algorithm": [
        "A step-by-step method",
        "It is used to solve problems",
        "Computer programs use many of them"
    ],
    "computer": [
        "An electronic machine",
        "It processes data",
        "You are probably using one right now"
    ],
    "developer": [
        "A person who creates software",
        "They write and test code",
        "They can build apps and websites"
    ],
    "internet": [
        "A global network",
        "It connects computers around the world",
        "You are using it right now"
    ]
}

while True:
    secret_word = random.choice(list(words.keys()))
    clues = words[secret_word]

    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    score = 0
    clue_number = 0

    print("\nA new mystery case has been opened!")
    print("Find the secret word to solve the case!")

    while wrong_guesses < max_wrong_guesses and "_" in guessed_word:
        print("\n" + "-" * 50)
        print("Mystery Word:", " ".join(guessed_word))
        print("Lives:", max_wrong_guesses - wrong_guesses)

        if guessed_letters:
            print("Guessed Letters:", ", ".join(guessed_letters))
        else:
            print("Guessed Letters: None")

        print("Clue:", clues[clue_number])

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess

            score += 10

            if clue_number < 2:
                clue_number += 1

        else:
            wrong_guesses += 1
            score -= 2
            print("Wrong guess!")

    print("\n" + "=" * 50)

    if "_" not in guessed_word:
        print("CASE SOLVED!")
        print("You found the secret word!")
        print("Secret Word:", secret_word)
        print("Final Score:", score)

        if score >= 50:
            print("Detective Rank: MASTER DETECTIVE")
        elif score >= 30:
            print("Detective Rank: ELITE DETECTIVE")
        else:
            print("Detective Rank: ROOKIE DETECTIVE")

    else:
        print("CASE FAILED!")
        print("The secret word was:", secret_word)
        print("Final Score:", score)
        print("Don't give up, detective!")

    print("=" * 50)

    play_again = input("\nSolve another case? (yes/no): ").lower()

    if play_again != "yes":
        print("\nDetective session closed.")
        print("Thanks for playing Code Detective!")
        break
