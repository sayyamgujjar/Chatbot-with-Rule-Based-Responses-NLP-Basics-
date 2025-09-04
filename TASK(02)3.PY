print("🤖 Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user = input("You: ").lower()   # user input ko lowercase me convert
    if user == "exit":
        print("🤖 Chatbot: Goodbye! Have a nice day.")
        break

    # Rule-based responses
    if "hello" in user or "hi" in user:
        print("🤖 Chatbot: Hi, how can I help you?")
    elif "your name" in user:
        print("🤖 Chatbot: I am your Python Chatbot.")
    elif "how are you" in user:
        print("🤖 Chatbot: I'm just code, but I'm doing fine 😃.")
    elif "weather" in user:
        print("🤖 Chatbot: Sorry, I can't give live weather yet.")
    elif "bye" in user:
        print("🤖 Chatbot: Bye! Take care.")
    else:
        print("🤖 Chatbot: I don’t understand.")
