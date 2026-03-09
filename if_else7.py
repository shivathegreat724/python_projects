
"""Write a program to select a ride according to your preference. The ride is divided into two 
major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. 
To give the user better selection options."""

print("Choose a mode of transport that you like the most.")
print("1. Bike")
print("2. Car")
choiceone = int(input(" 1 or 2? "))
if choiceone == 1:
    print("1. Scooty")
    print("2. Bike")
    a = int(input(" 1 or 2?"))
    if a == 1:
        print("You chose Scooty.")
    else:
        print("You chose Bike.")
elif choiceone == 2:
    print("1. SUV")
    print("2. Sedan")
    a = int(input(" 1 or 2?"))
    if a == 1:
        print("You chose SUV.")
    else:
        print("You chose Sedan.")
else:
    print("Invalid Input!")

