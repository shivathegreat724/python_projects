"""Define a function to find a cube and define another function which let execute the cube function if the number is 
divisible by 3
"""
# Code
def cube(number):
    return number * number * number
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))


