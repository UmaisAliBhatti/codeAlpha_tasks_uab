
def reply(text):
    text = text.lower().strip()

    if text == "hello" or text == "hi":
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I'm just a small chatbot."
    elif text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."


print("Chatbot started. Say hello, ask 'how are you', or say bye to quit.")

while True:
    user = input("You: ")
    answer = reply(user)
    print("Bot:", answer)

    if answer == "Goodbye!":
        break
