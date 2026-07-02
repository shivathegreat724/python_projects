from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()

window.title("Shiva Docs")
window.geometry("600x500")
window.rowconfigure(0, minsize = 800, weight = 1)
window.columnconfigure(1, minsize = 800, weight = 1)

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Shiva Docs - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaultextension= "txt", 
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Shiva Docs - {filepath}")
txt_edit = Text(window) 
fr_buttons = Frame(window, relief=RAISED, bd = 2)
btn1 = Button(fr_buttons, text = "Open", command = open_file)
btn2 = Button(fr_buttons, text = "Save as", command = save_file)
btn1.grid(row = 0, column = 0, sticky= "ew", padx=5, pady=5)
btn2.grid(row = 1, column = 0, sticky= "ew", padx=5)
fr_buttons.grid(row = 0, column = 0, sticky="ns")
txt_edit.grid(row = 0, column = 1, sticky= "nsew")
window.mainloop()


