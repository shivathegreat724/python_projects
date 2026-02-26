"""Write a program to calculate the number of notes in the given
 amount?"""
Amount =int(input("Please Enter Amount for Withdraw :"))

notes_of_100 = Amount//100
notes_of_50= (Amount%100)//50
notes_of_10= ((Amount%100)%50)//10
remaining_amount= (((Amount%100)%50)%10)


print( "notes of 100 " , notes_of_100)
print("notes of 50 " , notes_of_50)
print("notes of 10 " , notes_of_10)
print("remaining amount" , remaining_amount)