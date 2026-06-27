from tkinter import *
from datetime import date
screen = Tk()
screen.geometry("900x500")
screen.title("Age Calculator")
mainlbl = Label(screen, text="Enter your birth date:", bg="#0084FF", height=3, width=100)
lbl1 = Label(screen, text="Day:", bg="#FD4848", height=1,width=20)
lbl2 = Label(screen, text="Month:", bg="#FD4848", height=1, width=20)
lbl3 = Label(screen, text="Year:", bg="#FD4848", height=1, width=20)
Day_entry = Entry(screen)
Month_entry = Entry(screen)
Year_entry = Entry(screen)
textbox = Text(screen, height=5, width=40)
def display():
    day = int(Day_entry.get())
    month = int(Month_entry.get())
    year = int(Year_entry.get())
    birth_date = date(year, month, day)
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    textbox.delete("1.0", END)
    textbox.insert(END, f"You are {age} years old.")
mainlbl.pack()
lbl1.pack()
Day_entry.pack()
lbl2.pack()
Month_entry.pack()
lbl3.pack()
Year_entry.pack()
textbox.pack()
Button(screen, text="Calculate Age", command=display).pack()
screen.mainloop()