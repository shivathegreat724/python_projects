# 1) Take an integer input from the user and store it in `rows`.

# (This represents the total number of rows to print.)

# 2) Initialize `number = 1`.

# (This is the starting value to be printed in Floyd's Triangle.)

# 3) Print a heading message: "Floyd's Triangle".

# 4) Use an outer loop to handle each row from 1 to `rows` (inclusive):

# a) The current row number is `i`.

# 5) Use an inner loop to handle the numbers in each row:

# a) For row `i`, print `i` numbers, so loop `j` from 1 to `i` (inclusive).

# b) Print the current value of `number` on the same line using `end=' '`.

# c) Increase `number` by 1 after printing so the next number continues in sequence.

# 6) After finishing each row, print a blank `print()` to move to the next line.

rows = int(input("Enter a number:"))
number = 1
print("Floyd's Triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number = number + 1
    print()