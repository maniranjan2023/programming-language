import random

# List of words to choose from
words = ["python", "hangman", "development", "programming", "databases", "artificial", "algorithm", "network", "syntax", "compiler"]

def choose_word():
    return random.choice(words)

def display_progress(word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)

def hangman_game():
    word_to_guess = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")
    print(display_progress(word_to_guess, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess! You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")

        print(display_progress(word_to_guess, guessed_letters))

        # Check if the player has guessed all the letters in the word
        if set(word_to_guess) <= guessed_letters:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("Sorry, you've run out of guesses. The word was:", word_to_guess)

# Run the game
if __name__ == "__main__":
    hangman_game()
