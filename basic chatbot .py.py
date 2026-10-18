print("Bot: Hi! I'm RuleBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    elif user_input == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm just a program, but doing great!")

    elif user_input == "name":
        print("Bot: I am RuleBot, your AI-like assistant.")

    elif user_input == "help":
        print("Bot: Try: hello, how are you, name, bye")

    elif user_input == "thanks":
        print("Bot: You're welcome!")

    elif user_input == "what can you do":
        print("Bot: I can answer simple questions.")

    elif user_input == "age":
        print("Bot: I don't have an age. I am a chatbot.")

    elif user_input == "time":
        print("Bot: I cannot check the current time.")

    elif user_input == "school":
        print("Bot: I can help you with basic school questions.")

    else:
        print("Bot: Sorry, I don't understand that.")