import random
import tkinter as tk
battlescreen = tk.Tk()
battlescreen.geometry("500x600")
tk.Label(text = "😠⚔️😠", width=20, height=3, font= ("Segoe UI Emoji", 30)).pack()
result = tk.Label(text="", font=("Arial", 14))
result.pack()
def play(user):
    computer = random.choice(["rock", "paper", "scissors"])
    if user == computer:
        winner = "Tie!"
    elif user == "rock" and computer == "scissors":
        winner = "You win!"
    elif user == "paper" and computer == "rock":
        winner = "You win!"
    elif user == "scissors" and computer == "paper":
        winner = "You win!"
    else:
        winner = "Computer wins!"
    result.config(text=f"You: {user}\nComputer: {computer}\n{winner}")
tk.Button(text="ROCK", bg = "#565F66", width = 10, height=3, command=lambda: play("rock")).pack(pady=20)
tk.Button(text="PAPER", bg = "#D1C2A9", width = 10, height=3, command=lambda: play("paper")).pack(pady=20)
tk.Button(text="SCISSORS",bg = "#F9574F", width = 10, height=3, command=lambda: play("scissors")).pack(pady=20)
battlescreen.mainloop()