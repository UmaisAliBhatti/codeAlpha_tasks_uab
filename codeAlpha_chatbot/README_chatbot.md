# Task 4: Basic Chatbot

A simple rule-based chatbot written in Python. It replies to a few known phrases with predefined answers.

## How to Run

```
python chatbot_simple.py
```

Requires Python 3. No extra packages needed.

## How to Use

Type a message and press Enter. The bot replies. Say `bye` to end the chat.

## Supported Phrases

| You type            | Bot replies                |
|---------------------|----------------------------|
| `hello` or `hi`     | Hi!                        |
| `how are you`       | I'm fine, thanks!          |
| `what is your name` | I'm just a small chatbot.  |
| `bye`               | Goodbye!                   |
| anything else       | Sorry, I don't understand. |

Input is not case-sensitive, so `Hello` and `HELLO` both work. The phrase must match exactly, so `hello there` gets the fallback reply.

## Example

```
Chatbot started. Say hello, ask 'how are you', or say bye to quit.
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: bye
Bot: Goodbye!
```

## Adding New Replies

Open `chatbot_simple.py` and add another `elif` inside the `reply()` function:

```python
elif text == "what can you do":
    return "I can chat a little!"
```

## Concepts Used

- `if` / `elif` / `else` (choosing a reply)
- Functions (`reply()`)
- `while` loop (keeps the chat going until goodbye)
- Input / output

## Files

| File | Description |
|------|-------------|
| `chatbot_simple.py` | The chatbot script |
