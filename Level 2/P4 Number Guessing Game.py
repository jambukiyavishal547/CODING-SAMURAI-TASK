import tkinter as tk
import random

# Initial values
secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts

    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if guess < secret_number:
            result_label.config(text="📉 Too Low!", fg="blue")
        elif guess > secret_number:
            result_label.config(text="📈 Too High!", fg="orange")
        else:
            result_label.config(
                text=f"🎉 Correct! You guessed it in {attempts} attempts!",
                fg="green"
            )
            guess_button.config(state="disabled")

    except ValueError:
        result_label.config(text="❌ Enter a valid number", fg="red")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    attempts_label.config(text="Attempts: 0")
    result_label.config(text="Game Reset! Start guessing 🎯", fg="black")
    guess_button.config(state="normal")

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("420x360")
root.config(bg="#f2f2f2")

# Title
title_label = tk.Label(
    root,
    text="🎲 Number Guessing Game",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2"
)
title_label.pack(pady=10)

# Instruction
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 11),
    bg="#f2f2f2"
)
instruction_label.pack()

# Entry
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=8)

# Buttons
guess_button = tk.Button(
    root,
    text="Guess",
    font=("Arial", 11),
    width=12,
    command=check_guess
)
guess_button.pack(pady=5)

reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 11),
    width=12,
    command=reset_game
)
reset_button.pack(pady=5)

# Attempts
attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 11),
    bg="#f2f2f2"
)
attempts_label.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="Start guessing 🎯",
    font=("Arial", 12),
    bg="#f2f2f2"
)
result_label.pack(pady=10)

# Rules Section
rules_label = tk.Label(
    root,
    text=(
        "📜 Rules:\n"
        "• Guess a number between 1 and 100\n"
        "• Feedback will guide you\n"
        "• Attempts are counted\n"
        "• Reset to play again"
    ),
    font=("Arial", 10),
    bg="#f2f2f2",
    justify="left"
)
rules_label.pack(pady=10)

# Run app
root.mainloop()
