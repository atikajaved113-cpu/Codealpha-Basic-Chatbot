def chatbot_response(message):#function to check a user message and return a suitable reply
    message = message.lower().strip()#convert the message lowercase and remove extra spaces

    if message in ["hello", "hi", "hey"]:#check if the user says hi,hello or hey
        return "Hi! How can I help you?"

    elif message in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"

    elif message in ["i am fine", "i'm fine", "fine"]:
        return "Glad to hear that!"

    elif message == "help":
        return "You can say hello, ask how I am, or type bye."

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand. Please try another message."


print("Welcome to the Basic Chatbot!")#display the welcome message
print("Type 'help' for help or 'bye' to exit.")#type a bye if the user wants to stop the conversion

while True:
    user_message = input("You: ")#call a function

    response = chatbot_response(user_message)

    print("Bot:", response)#display the chatbot reply

    if user_message.lower().strip() in [
        "bye", "goodbye", "exit", "quit"
    ]:
        break#end of the chatbot programe