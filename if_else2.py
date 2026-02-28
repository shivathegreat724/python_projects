sellcost = int(input("Enter you selling cost:"))
buycost = int(input("Enter you buying cost:"))
if sellcost> buycost:
    profit = sellcost -buycost
    print("Your profit is,",profit)
elif sellcost< buycost:
    loss = buycost -sellcost
    print("Your loss is,",loss)
else:
    print("No gain, no loss.")
