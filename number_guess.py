import random
playing = True
number = str(random.randint(0, 9))
print("Instructions: Guess the number and see if it matches with the answer. Otherwise, restart.")
while(playing):
    guess = (input("Enter a number a number between 0 to 9:"))
    if number == guess:
        print("Well Done")
        print(f"The secret number was {number}")
        break
    else:
        print("Try again")
