"""Write a program to reverse the string entered by the user."""

#Code
string = str(input("Enter a word or sentence:"))
string2 = ""
for i in string:
    string2 = i + string2
print(string)
print(string2)

