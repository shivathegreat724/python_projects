try:
    num1,num2 = eval(input("Enter two numbers that are seperate by a space comma:"))
    result = num1 / num2
    print(result)
except ZeroDivisionError as zero:
    print(f"Division by {zero} is unavailable!!")
except SyntaxError as syntax:
    print(f"Here is your mistake: {syntax}.")
except:
    print("Wrong Input")
else:
    print("No exceptions occured.")
finally:
    print("This will execute no matter what. ($_$)")
