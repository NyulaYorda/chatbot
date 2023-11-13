import random

def greet():
    greetings = ["Hello!", "Hi there!", "Greetings!" , "Hey"]
    print(random.choice(greetings))

def chatbot_response(user_input):
    responses = {
        "how are you": "I'm just a computer program, but thanks for asking!",
        "what's your name": "I'm a chatbot. You can call me Beela ChatBot.",
        "bye": "Goodbye! Have a great day!",
    }

    # Check if the user input matches any predefined responses
    for key, value in responses.items():
        if key in user_input.lower():
            return value

    # If no predefined response, provide a default response
    return "I'm not sure how to respond to that. Ask me something else!"

if __name__ == "__main__":
    greet()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot_response(user_input)
        print("Beela ChatBot:", response)
