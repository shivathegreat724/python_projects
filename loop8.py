"""Write a program to print all the prime numbers which come in the range entered by the user?
"""
lower = int(input("Enter a lower number:"))
upper = int(input("Enter a higher number:"))
print(lower, upper)
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "is prime")
        