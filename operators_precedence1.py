v = 4
w = 5
x = 8
y = 2
z = (v + w) * x / y
print(z)
name = "Alex"
age = 0
if name == "Alex" or (name == "John" and age >= 2):
    print("Hello, welcome!")

numn = int(input("Enter a Numerator:"))
numd = int(input("Enter a Denominator:"))
if numn % numd == 0:
    print(f"{numn} is divisible by {numd}")
else:
    print(f"{numn} is not divisible by {numd}")

a = int(input("Enter a value:"))
b = int(input("Enter a value:"))
c = int(input("Enter a value:"))
avg = (a + b + c) / 3
print("Average =", avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is higher than %d" %(avg, a))
elif avg > b:
    print("%d is higher than %d" %(avg, b))
elif avg > c:
    print("%d is higher than %d" %(avg, c))
else:
    print("Invalid Input!")

mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40
sum = mean1 * total_number
print("The sum of the 40 numbers are" ,sum)
num2 = sum - ((wrong_number) - (correct_number))
print("num2")
mean2 = num2/total_number
print(mean2)
