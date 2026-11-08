# Task 1: Hangman Game

A simple text-based Hangman game written in Python. The player guesses a hidden word one letter at a time.

## How to Run

```
python hangman_simple.py
```

Requires Python 3. No extra packages needed.

## How to Play

1. The computer picks a random word from a small list of 5 words.
2. The word is shown as underscores, one for each letter.
3. Type one letter at a time to guess.
4. A correct guess fills in the letter wherever it appears.
5. A wrong guess adds to your wrong-guess count.
6. You win by revealing the whole word. You lose after 6 wrong guesses.

## Features

- 5 predefined words: python, hangman, keyboard, program, computer
- Maximum of 6 incorrect guesses
- Shows the letters you have already tried
- Rejects invalid input (more than one character, numbers, symbols)
- Tells you if you repeat a guess
- Console input/output only, with no graphics or audio

## Example

```
Welcome to Hangman!
The word has 6 letters. You can miss 6 times.

_ _ _ _ _ _
Wrong guesses: 0 / 6
Letters tried: []
Guess a letter: p
Nice, that letter is in the word!

p _ _ _ _ _
```

## Concepts Used

- `random` module (picking a random word)
- `while` loop (main game loop)
- `if` / `elif` / `else` (checking guesses)
- Strings (building the displayed word)
- Lists (words and guessed letters)

## Files

| File | Description |
|------|-------------|
| `hangman_simple.py` | The game script |
