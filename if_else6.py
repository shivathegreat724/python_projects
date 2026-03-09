"""Write a program to check whether the student can take an exam or not. 
Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and
‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is
above 75, then allowed; otherwise, not allowed."""

one_con = input("Do you have a medical issue?")
two_con = int(input("Enter your attendance percentage:"))
if one_con == "Y":
    print("Yes, you are eligible.")
else:
   if two_con >= 75:
       print("Yes, you are eligible.")
   else:
       print("No, you are not eligible.")   

    