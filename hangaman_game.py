# Import random module
import random

#List of words
words = ["apple", "tiger", "chair", "bread", "plane"]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")

    elif guess in secret_word:
        guessed_letters.append(guess)
        print("✅ Correct!")

    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("\n💀 You lost!")
    print("The word was:", secret_word)