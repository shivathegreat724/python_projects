
"""Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. 
Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function 
calculates the total amount you should pay.
"""
#Code
def totlal_calc(bill_amount, tip_perc):
    total = (0.01 * tip_perc + 1) * bill_amount
    total = round(total, 2)
    print(f"Your total is {total}.")
totlal_calc(150, 20)

