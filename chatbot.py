# Python Project - 02 Personal Chat Assistant

def chatbot():

    print("======================================")
    print("       PERSONAL CHAT ASSISTANT")
    print("======================================")
    print("Ask me questions about Python, AI, CSE,")
    print("college, and basic programming.")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ")

        question = user_input.lower()

        # Greeting
        if question in ["hi", "hello", "hey"]:
            print("Bot: Hello! 😊 How can I help you?")

        # Python
        elif "what is python" in question or "python" == question:
            print("Bot:", user_input)
            print("Bot: Python is a popular programming language.")
            print("Bot: It is widely used in AI, ML, data science,")
            print("Bot: web development, and automation.")

        # AI
        elif "what is ai" in question or "artificial intelligence" in question:
            print("Bot:", user_input)
            print("Bot: AI stands for Artificial Intelligence.")
            print("Bot: It allows computers to perform tasks that")
            print("Bot: normally require human intelligence.")

        # Machine Learning
        elif "what is machine learning" in question or "machine learning" in question:
            print("Bot:", user_input)
            print("Bot: Machine Learning is a part of AI.")
            print("Bot: It allows computers to learn patterns from")
            print("Bot: data and make predictions or decisions.")

        # CSE
        elif "what is cse" in question or "computer science" in question:
            print("Bot:", user_input)
            print("Bot: CSE stands for Computer Science and Engineering.")
            print("Bot: It includes programming, algorithms, databases,")
            print("Bot: operating systems, networks, AI, and software development.")

        # Python uses
        elif "python uses" in question or "use of python" in question:
            print("Bot:", user_input)
            print("Bot: Python can be used for:")
            print("Bot: 1. Artificial Intelligence")
            print("Bot: 2. Machine Learning")
            print("Bot: 3. Data Science")
            print("Bot: 4. Web Development")
            print("Bot: 5. Automation")

        # Your name
        elif "your name" in question:
            print("Bot:", user_input)
            print("Bot: I am your Personal Chat Assistant.")

        # How are you
        elif "how are you" in question:
            print("Bot:", user_input)
            print("Bot: I'm doing great! 😊 Thanks for asking.")

        # What can you do
        elif "what can you do" in question:
            print("Bot:", user_input)
            print("Bot: I can answer basic questions about Python,")
            print("Bot: AI, Machine Learning, and Computer Science.")

        # Thanks
        elif "thank" in question:
            print("Bot:", user_input)
            print("Bot: You're welcome! 😊")

        # Exit
        elif question == "bye":
            print("Bot:", user_input)
            print("Bot: Goodbye! 👋 Have a great day!")
            break

        # Unknown question
        else:
            print("Bot:", user_input)
            print("Bot: Sorry, I don't know the answer to that yet.")
            print("Bot: Try asking me about Python, AI, ML, or CSE.")

        print()


chatbot()