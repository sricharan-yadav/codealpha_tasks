import re
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext
import random

# Function to generate chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    # Exit
    if re.search(r"\b(bye|exit|quit)\b", user_input):
        return "Goodbye! Have a nice day 😊"

    # Greetings
    elif re.search(r"\b(hi|hello|hey)\b", user_input):
        return random.choice(["Hello! How can I help you today?", "Hey there 👋", "Hi! Nice to see you."])

    # Name
    elif re.search(r"\b(your name|who are you)\b", user_input):
        return "I am a simple chatbot created using Python."

    # How are you
    elif re.search(r"\b(how are you|how's it going)\b", user_input):
        return random.choice(["I'm doing great! How about you?", "I’m just code, but I feel awesome 😎", "Always good when chatting with you!"])

    # Time
    elif re.search(r"\b(time|current time|what's the time)\b", user_input):
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."

    # Date
    elif re.search(r"\b(date|today)\b", user_input):
        today = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}."

    # Thanks
    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return random.choice(["You're welcome! 😊", "No problem!", "Anytime!"])

    # Jokes
    elif re.search(r"\b(joke|funny)\b", user_input):
        jokes = [
            "Why don’t skeletons fight each other? Because they don’t have the guts 😂",
            "I told my computer I needed a break, and it said 'No problem — I’ll go to sleep!' 😴",
            "Why was the math book sad? Because it had too many problems 😆"
        ]
        return random.choice(jokes)

    # Weather (dummy response)
    elif re.search(r"\b(weather|rain|sunny)\b", user_input):
        return "I can’t check live weather yet 🌦️, but I hope it’s nice where you are!"

    # Creator
    elif re.search(r"\b(who created you|your creator|developer)\b", user_input):
        return "I was created by a Python programmer 👨‍💻."

    # Age
    elif re.search(r"\b(your age|how old)\b", user_input):
        return "I was born just a few seconds ago when you ran me 🍼."

    # Default
    else:
        return "Sorry, I didn’t understand that. Can you rephrase?"

# Function to send message
def send_message(user_input=None):
    if user_input is None:
        user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    response = get_response(user_input)
    chat_area.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    # Exit if user says bye
    if re.search(r"\b(bye|exit|quit)\b", user_input.lower()):
        root.after(1000, root.destroy)

# GUI Setup
root = tk.Tk()
root.title("Rule-Based Chatbot 🤖")
root.geometry("550x600")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Quick reply buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Quick reply buttons
quick_replies = ["Hi", "How are you?", "What's the time?", "Date", "Tell me a joke", "Your name", "Bye"]

for text in quick_replies:
    btn = tk.Button(button_frame, text=text, width=15, command=lambda t=text: send_message(t))
    btn.pack(side=tk.LEFT, padx=5)

# Bind Enter key
root.bind("<Return>", lambda event: send_message())

# Run chatbot GUI
root.mainloop()
