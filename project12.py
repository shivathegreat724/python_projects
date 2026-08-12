import random
from colorama import init, Fore, Style
init(autoreset=True)
winning_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}
def whoWin(user_chioice, computer_choice):
    if user_chioice == computer_choice:
        return "Tie"
    elif winning_rules[user_chioice] == computer_choice:
        return "User"
    else:
         return "Computer"
def main():
    user_score = 0
    computer_score = 0
    ties = 0
    while(True):
        user_choice = input("Choose either rock/paper/scissors:")
        computer_choice = random.choice(['rock', 'paper' , 'scissors'])
        if user_choice == "quit":
            print(Fore.RED + "Thank you for playing")
            print(Fore.MAGENTA + Style.BRIGHT +  "SCOREBOARD")
            print(Fore.GREEN + f"User scored {user_score}.")
            print(Fore.BLUE + f"Computer scored {computer_score}.")
            print(Fore.YELLOW + f"Ties =  {ties}.")
            break
        print(Fore.GREEN + f"User choice is {user_choice}.")
        print(Fore.BLUE + f"Computer choice is {computer_choice}.")
        result = whoWin(user_choice, computer_choice)
        if result == "Tie":
            print(Fore.YELLOW + "It is a tie.")
            ties = ties + 1
        elif result == "User":
            print(Fore.GREEN + "User wins.")
            user_score = user_score + 1
        else:
            print(Fore.BLUE + "Computer wins.")
            computer_score = computer_score + 1
main()



