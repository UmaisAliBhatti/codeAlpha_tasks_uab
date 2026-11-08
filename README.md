# CodeAlpha Python Internship Tasks

This repository contains my work for the **CodeAlpha Python Programming Internship**. It includes four small console-based projects that practise core Python concepts: loops, conditionals, dictionaries, functions, file handling and standard-library modules.

## Projects

| # | Project | Script | What it does |
|---|---------|--------|--------------|
| 1 | Hangman Game | `hangman_simple.py` | Guess a hidden word one letter at a time, with a limit of 6 wrong guesses |
| 2 | Stock Portfolio Tracker | `stock_tracker_simple.py` | Calculates the total value of a portfolio from hardcoded stock prices and can save it to a file |
| 3 | Task Automation (JPG Mover) | `move_jpgs_simple.py` | Moves all `.jpg` files from a folder into a new folder |
| 4 | Basic Chatbot | `chatbot_simple.py` | Rule-based chatbot with predefined replies |

Each project has its own README with more detail (see the links below).

## Getting Started

### Requirements

- Python 3.x
- No external libraries are needed. Everything uses the Python standard library.

### Clone the repository

```
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### Run a project

```
python hangman_simple.py
python stock_tracker_simple.py
python move_jpgs_simple.py
python chatbot_simple.py
```

On some systems you may need to use `python3` instead of `python`.

## Project Details

### Task 1: Hangman Game
A text-based word-guessing game.
- Picks a random word from a list of 5 predefined words
- Allows a maximum of 6 incorrect guesses
- Validates input and tracks letters already tried
- **Concepts:** `random`, `while` loop, `if-else`, strings, lists
- [Read more](README_hangman.md)

### Task 2: Stock Portfolio Tracker
Calculates total investment value from stock names and quantities entered by the user.
- Prices are stored in a hardcoded dictionary
- Shows each holding and the total value
- Optionally saves the result to `portfolio.txt`
- **Concepts:** dictionary, input/output, basic arithmetic, file handling
- [Read more](README_stock_tracker.md)

### Task 3: Task Automation with Python
Automates a repetitive real-life task: organising image files.
- Moves every `.jpg` file into a new `jpg_images` folder
- Creates the folder automatically and never overwrites existing files
- **Concepts:** `os`, `shutil`, file handling
- [Read more](README_jpg_mover.md)

### Task 4: Basic Chatbot
A simple chatbot that answers known phrases such as "hello", "how are you" and "bye".
- Case-insensitive matching
- Fallback reply for unknown input
- **Concepts:** `if-elif`, functions, loops, input/output
- [Read more](README_chatbot.md)

## Repository Structure

```
.
├── README.md
├── hangman_simple.py
├── README_hangman.md
├── stock_tracker_simple.py
├── README_stock_tracker.md
├── move_jpgs_simple.py
├── README_jpg_mover.md
├── chatbot_simple.py
└── README_chatbot.md
```

## Skills Practised

- Writing clean, readable Python
- Using loops and conditional logic
- Working with lists, dictionaries and strings
- Reading user input and validating it
- File and folder handling with `os` and `shutil`
- Breaking a problem into functions

## About

Completed as part of the CodeAlpha Python Programming internship.

**Author:** _Your Name_
**GitHub:** [@your-username](https://github.com/your-username)
**LinkedIn:** _Your LinkedIn URL_

## License

This project is open source and available for learning purposes.
