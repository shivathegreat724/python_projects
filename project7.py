from tkinter import *
window = Tk()
window.title("Length Converter")
window.geometry("500x500")
lbl1 = Label(text = "Inches", bg = "#0084FF", height = 3, width = 50)
lbl1_entry = Entry(window)
lbl2 = Label(text = "Centimeters", bg = "#0084FF", height = 3, width = 50)
def display():
    inches = float(lbl1_entry.get())
    centimetres = f"{inches * 2.54}cm"
    textbox.insert(END, centimetres)
textbox = Text(window, height=3, width=100)
lbl1.pack()
lbl1_entry.pack()
lbl2.pack()
textbox.pack()
Button(window, text="Convert", command=display).pack()
window.mainloop()


