from tkinter import *
from tkinter import messagebox
calc = Tk()
calc.geometry("400x350")
calc.title("Denomination Calculator")
calc.config(bg = "lightblue")
Label(calc, text="Denomination Calculator", font = ("Arial", 16, "bold"), bg = "lightblue").pack(pady = 20)
def topwin():
    top = Toplevel(calc)
    top.title("Calculator")
    top.geometry("300x300")
    top.config(bg = "lightgrey")
    Label(top, text="Enter amount:", bg = "lightgrey").pack()
    e = Entry(top)
    e.pack()
    out = {}
    for d in (2000, 500, 100):
        Label(top, text=f"{d} notes", bg = "lightgrey").pack()
        out[d] = Entry(top)
        out[d].pack()
    def calculator():
        try:
            amt = int(e.get())
            for d in (2000, 500, 100):
                out[d].delete(0,END)
                out[d].insert(0, amt // d)
                amt%= d
        except:
            messagebox.showerror("ERROR", "Invalid amount")
    Button(top, text="Calculate", command = calculator, bg = "brown", fg = "white").pack(pady=10)
Button(calc, text="Get Starting", command = topwin, bg = "red", fg = "white").pack(pady=20)
calc.mainloop()



