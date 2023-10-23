import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while True:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            if attempts == 0:
                print(f"Out of attempts! The word was: {word}")
                break

if __name__ == "__main__":
    hangman()
