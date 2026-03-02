h = float(input("Height(cm) :"))
w = float(input("Weight (kg):"))
BMI = w / (h / 100) ** 2
print(BMI, "is your BMI")
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are severely overweight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely OBESE!")
