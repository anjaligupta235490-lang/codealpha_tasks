from datetime import datetime
import random
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why do Java developers wear glasses? Because they don't C#."
]

facts = [
    "Python was created by Guido van Rossum.",
    "The first computer programmer was Ada Lovelace.",
    "Python is one of the most popular programming languages."
]

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a simple chatbot created to assist you.",
    "thank you": "You're welcome!",
    "good morning": "Good Morning! Have a wonderful day.",
    "good night": "Good Night! Sweet dreams.",
    "who created you": "I was created by Anjali Gupta using Python.",
    "what can you do": "I can answer simple questions, tell jokes, share facts, and show the current date and time."
}

def welcome():
    print("=" * 50)
    print("        WELCOME TO BASIC CHATBOT")
    print("=" * 50)
    print("Type 'help' to see available commands.")
    print("Type 'exit' to end the conversation.\n")

def help_menu():
    print("\n========== AVAILABLE COMMANDS ==========")
    print("hello              - Greet the bot")
    print("hi                 - Say Hi")
    print("how are you        - Ask about the bot")
    print("what is your name  - Know the bot's name")
    print("thank you          - Thank the bot")
    print("good morning       - Wish the bot")
    print("good night         - Say good night")
    print("who created you    - Know the creator")
    print("what can you do    - Know the bot's abilities")
    print("tell me a joke     - Hear a funny joke")
    print("tell me a fact     - Learn an interesting fact")
    print("date               - Show today's date")
    print("time               - Show current time")
    print("help               - Show all commands")
    print("exit               - Close the chatbot")
    print("bye                - End the conversation")
    print("========================================\n")

def chatbot():
    name = input("Bot: What's your name? ").strip().title()
    print(f"Bot: Hello, {name}! Nice to meet you.\n")
    print("Bot: Type 'help' anytime to see all available commands.\n")
    count = 0
    while True:
        user_input = " ".join(input("You: ").strip().lower().split())
        count += 1
        if user_input == "exit" or user_input == "bye":
            print(f"Bot: We exchanged {count} messages.")
            print("Bot: Thank you for chatting with me!")
            print("Bot: Have a wonderful day!")
            print("Bot: Goodbye!")
            break
        

        elif user_input == "tell me a joke":
            print("Bot:", random.choice(jokes))
        
        elif user_input == "tell me a fact":
            print("Bot:", random.choice(facts))
        
        elif user_input == "time":
            current_time = datetime.now().strftime("%I:%M:%S %p")
            print(f"Bot: Current time is {current_time}")

        elif user_input == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {current_date}")

        elif user_input == "help":
            help_menu()

        elif user_input in responses:
            print("Bot:", responses[user_input])


        else:
            print("Bot: Sorry, I don't understand that.")
            print("Bot: Type 'help' to see the available commands.")
welcome()
chatbot()
        