from tkinter import *
window = Tk()
window.title("Password Checker App")
window.geometry("500x500")
password = Entry(window)
def topwin():
    top = Toplevel(window)
    top.title("Computer's Decision")
    top.geometry("500x500")
    lbl1 = Label(top, text="GREAT", bg="darkgreen", fg="white",
                 width=75, height=5, font=("Kaushan Script", 14))
    lbl1.pack(padx=20, pady=20)
    lbl2 = Label(top, text="OK", bg="goldenrod", fg="white",
                 width=75, height=5, font=("Kaushan Script", 14))
    lbl2.pack(padx=20, pady=20)
    lbl3 = Label(top, text="BAD", bg="darkred", fg="white",
                 width=75, height=5, font=("Kaushan Script", 14))
    lbl3.pack(padx=20, pady=20)
    pw = password.get()
    if len(pw) > 8:
        lbl1.config(bg="lime")
    elif len(pw) >= 6 and len(pw) <= 8:
        lbl2.config(bg="yellow")
    elif len(pw) >= 1 and len(pw) <= 5:
        lbl3.config(bg="red")
Button(text="Click here", command=topwin, width=25, height=25).pack(padx=25, pady=25)
password.pack()
window.mainloop()