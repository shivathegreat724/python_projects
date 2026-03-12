
"""Write a program to print the numbers in reverse order beginning from the number entered by 
the user."""

#Code
n = int(input("Enter a number > 1:"))
print("The numbers shall be shown in reverse.")
for i in range(n, 0, - 1):
    print(i)