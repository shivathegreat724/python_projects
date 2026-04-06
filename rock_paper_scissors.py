import random
while(True):
    user_action = input("Choose between either rock, paper or scissors:")
    r = "rock"
    p = "paper"
    s = "scissors"
    possible_actions = r,p,s
    computer_action = random.choice(possible_actions)
    print(f"User = {user_action} and Computer = {computer_action}")
    if user_action == computer_action:
        print("It is a tie.")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input!")
    elif user_action == r and computer_action == p:
        print("Computer Wins")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input!")
    elif user_action == p and computer_action == r:
        print("User Wins")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input")
    elif user_action == s and computer_action == p:
        print("User Wins")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input!")
    elif user_action == r and computer_action == s:
        print("User Wins")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input!")
    elif user_action == p and computer_action == s:
        print("Computer Wins")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input!")   
    elif user_action == s and computer_action == r:
        print("Computer Wins")
        play_again = input("Would you like to play again?")
        if play_again.lower() == "yes":
            print("Continue>")
            continue
        elif play_again.lower() == "no":
            break
        else:
            print("Invalid Input!")
    

            
    