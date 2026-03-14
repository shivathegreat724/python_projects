#Write a program to check if the number entered by the user is 
# an Armstrong number or not?
num = int(input("Enter a number:"))
sum = 0
temp = num
while(temp > 0):
    digit = temp % 10
    sum = sum + (digit * digit * digit)
    temp = temp // 10
if num == sum:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")