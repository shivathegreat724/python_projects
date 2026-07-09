import tkinter as tk
from tkinter import ttk, messagebox
bigmac = tk.Tk()
bigmac.title("Mc Donalds")
bigmac.geometry("320x450")
img = tk.PhotoImage(file= "images.png")
img = img.subsample(2, 2)
ttk.Label(bigmac, image = img).pack(pady = 5)
menu = {"Burger":10, "Fries":5, "Double Triple MAC":50}
entrys = {}
ttk.Label(bigmac, text = "Restaurant menu").pack(pady = 5)
for item, price in menu.items():
    frame = ttk.Frame(bigmac)
    frame.pack(pady=3)
    ttk.Label(frame, text=f"{item} - £{price}", width = 15).pack(side="left")
    entry = ttk.Entry(frame, width = 5)
    entry.pack(side="left")
    entrys[item] = entry
def place_order():
    total = 0
    bill = ""
    for item, price in menu.items():
        q = entrys[item].get()
        if q.isdigit() and int(q) > 0:
            cost = int(q) * price
            total += cost
            bill += f"{item}: = £{cost}\n"   
    if total == 0:
        messagebox.showerror("ERROR", "Enter a quantity")
    else:
        messagebox.showinfo("Bill:", bill + f"\nTotal = £{total}")
ttk.Button(bigmac, text = "Place Order", command = place_order).pack(pady=10)
bigmac.mainloop() 
