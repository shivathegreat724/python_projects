from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Main window")
def topwin():
    top = Toplevel()
    top.geometry("200x150")
    top.title("Top window")
    lbl1 = Label(top, text="Top level window")
    lbl1.pack()
    top.mainloop()
lbl2 = Label(root, text="This is a Root window")
btn = Button(root, text="Click me", command=topwin)
lbl2.pack()
btn.pack()
root.mainloop()

