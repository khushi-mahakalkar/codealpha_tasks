print("=" * 50)
print(" STUDY BUDDY CHATBOT")
print("=" * 50)
print("Hello! I am Study Buddy, your simple Python chatbot.")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.")
print("=" * 50)

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Ready to study?",
    "how are you": "I'm doing great! Thanks for asking.",
    "study": "Make a small study plan and focus on one topic at a time.",
    "motivate me": "Believe in yourself! Every small step takes you closer to your goal.",
    "python": "Python is a beginner-friendly programming language used in many fields.",
    "internship": "An internship is a great way to gain practical experience and build your skills.",
    "help": "You can ask me about study, Python, internships, motivation, or say hello.",
    "thank you": "You're welcome! Keep learning and keep growing!"
}

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input == "bye":
        print("Study Buddy: Goodbye! All the best with your studies! 👋")
        break

    found_response = False

    for keyword, response in responses.items():

        if keyword in user_input.split() or keyword == user_input:
            print("Study Buddy:", response)
            found_response = True
            break

        if " " in keyword and keyword in user_input:
            print("Study Buddy:", response)
            found_response = True
            break

    if not found_response:
        print("Study Buddy: I'm still learning! Try asking me something about study, Python, or motivation.")

print("\n" + "=" * 50)
print("            CHATBOT SESSION ENDED")
print("=" * 50)
