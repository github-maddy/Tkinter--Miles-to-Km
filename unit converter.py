from tkinter import *

window = Tk()
window.title("UNIT CONVERTER")

def km_calculate():
    value = float(input.get())
    km = 1.609 * value
    Label3.config(text=f"{km}")


input = Entry()
input.grid(column=2,row=1)

Label1 = Label(text="Miles")
Label1.grid(column=4,row=1)

Label2 = Label(text="is equal to ")
Label2.grid(column=1,row=2)

Label3 = Label(text="0")
Label3.grid(column=2,row=2)

Label4 = Label(text="Km")
Label4.grid(column=4,row=2)

Button = Button(text="Calculate",command=km_calculate)
Button.grid(column=2,row=3)

window.mainloop()