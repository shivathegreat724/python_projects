try:
    number = int(input("Enter a number:"))
    print("You have typed a number!!WELL DONE!!")
except ValueError as wrong:
    print(f"That are totally wrong: {wrong}.")