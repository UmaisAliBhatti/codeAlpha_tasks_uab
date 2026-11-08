
import random

words = ["python", "hangman", "keyboard", "program", "computer"]

word = random.choice(words)
guessed = []                            # letters the player already tried
wrong = 0                               # number of wrong guesses so far
max_wrong = 6

print("Welcome to Hangman!")
print("The word has", len(word), "letters. You can miss", max_wrong, "times.")

while wrong < max_wrong:
    # build the word with underscores for letters not guessed yet
    shown = ""
    for letter in word:
        if letter in guessed:
            shown = shown + letter + " "
        else:
            shown = shown + "_ "

    print()
    print(shown)
    print("Wrong guesses:", wrong, "/", max_wrong)
    print("Letters tried:", guessed)

    # if there are no underscores left, the player has won
    if "_" not in shown:
        print("You got it! The word was", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type just one letter.")
    elif guess in guessed:
        print("You already tried that one.")
    else:
        guessed.append(guess)
        if guess in word:
            print("Nice, that letter is in the word!")
        else:
            wrong = wrong + 1
            print("Nope, that letter is not in the word.")

# if the loop ended because of too many wrong guesses
if wrong == max_wrong:
    print()
    print("Game over! The word was", word)
