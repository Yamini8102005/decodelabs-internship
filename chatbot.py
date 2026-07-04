from datetime import datetime

# 🌸 Welcome Screen
print("\n🌸══════════════════════════════════════════════🌸")
print("              🌷 LOTUS CHATBOT 🌷")
print("         Your Friendly AI Assistant 💖")
print("🌸══════════════════════════════════════════════🌸")

print("\n✨ Hello! I'm Lotus.")
print("🌷 Ask me anything.")
print("💬 Type 'bye', 'exit', or 'quit' anytime to leave.\n")

# 🌸 Knowledge Base (Dictionary)
knowledge_base = {
    "hi": "🌸 Hello! Welcome to Lotus Chatbot! 💖",
    "hello": "🌸 Hello! Nice to see you! 😊",
    "hey": "🌸 Hey there! How can I help you today?",
    "how are you": "💖 I'm blooming beautifully today! How about you? 🌷",
    "your name": "🌸 My name is Lotus Chatbot.",
    "who created you": "💖 I was created by Yamini during her AI Internship at Decode Labs.",
    "ai": "🤖 AI stands for Artificial Intelligence. It helps machines learn and solve problems.",
    "python": "🐍 Python is a beginner-friendly and powerful programming language.",
    "thanks": "🌸 You're always welcome! 💖",
    "thank you": "🌸 Happy to help! 🌷",
    "good morning": "☀️ Good Morning! Have a wonderful day ahead. 🌸",
    "good night": "🌙 Good Night! Sweet dreams. 💖",
    "motivate me": "🌷 Believe in yourself. Every expert was once a beginner.",
    "joke": "😂 Why do programmers prefer Python? Because it's easy to learn! 🐍"
}

# 🌸 Exit Commands
exit_commands = ["bye", "exit", "quit"]

# 🌸 Chat Loop
while True:

    # Input Sanitization
    user = input("🌼 You : ").strip().lower()

    # Clean Exit
    if user in exit_commands:
        print("\n🌸 Lotus : Goodbye! 👋")
        print("💖 Stay happy and keep blooming! 🌷\n")
        break

    # Dynamic Responses
    elif user == "time":
        response = f"🕒 Current Time: {datetime.now().strftime('%I:%M %p')}"

    elif user == "date":
        response = f"📅 Today's Date: {datetime.now().strftime('%d-%m-%Y')}"

    # Dictionary Lookup
    else:
        response = knowledge_base.get(
            user,
            "🌸 Sorry! I don't understand that yet. Please try another question. 😊"
        )

    print(f"\n🌸 Lotus : {response}\n")