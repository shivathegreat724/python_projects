from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and time is", now)
print("\nDate componets", today.year, today.month, today.day)