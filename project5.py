from tkinter import *
window = Tk()
window.geometry("400x300")
window.configure(bg="#3895D3")
input1 = Label(window, text="First number:", bg="#3895D3")
input2 = Label(window, text="Second number:", bg="#3895D3")
input1Entry = Entry(window)
input2Entry = Entry(window)
text_box = Text(window, height=3, width=20)
def display():
    try:
        num1 = float(input1Entry.get())
        num2 = float(input2Entry.get())
        answer = int(num1 * num2)
        text_box.delete("1.0", END)     # Clear previous result
        text_box.insert(END, f"Ans: {answer}")
    except ValueError:
        text_box.delete("1.0", END)
        text_box.insert(END, "Please enter valid numbers")
btn = Button(window, text="Begin", command=display,
             height=1, bg="#1261A0", fg="white")
input1.pack()
input1Entry.pack()
input2.pack()
input2Entry.pack()
btn.pack(pady=10)
text_box.pack()
window.mainloop()