
# 1) Print a heading message for the pattern.

# 2) Take an integer input from the user and store it in `n`.

# (This represents the number of rows in the half pyramid.)

# 3) Use an outer loop to run from 0 to `n-1` (each iteration builds one row):

# a) For each row `i`, the number of stars to print is `i + 1`.

# 4) Use an inner loop to print stars in the current row:

# a) Run `j` from 0 to `i` (total `i + 1` times)

# b) Print "* " on the same line using `end=""` so it doesn’t go to the next line.

# 5) After finishing the inner loop for a row, print a blank `print()`

# to move the cursor to the next line for the next row.

print("Right angle triangle")
n = int(input("Enter a number:"))
for i in range(0, n):
    for j in range(i + 1):
        print("*",end = " ")
    print()