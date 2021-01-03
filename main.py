from tkinter import *

window = Tk()

window.title("GUI Program")
window.minsize(width=720,height=480)
window.maxsize(width=1420, height=1080)

response = "Label"

my_label = Label(text=f"{response}", font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

def button_clicked():
    print("Activated")
    my_label.config(text="Button was Clicked")
    print(input.get())

my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1,row=1)

my_button2 = Button(text="Click", command=button_clicked)
my_button2.grid(column=0, row=2)

input = Entry(width=10)
input.grid(column=2,row=3)

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# print(add(1,4,5,10,13,12))






















#Always at end of program
window.mainloop()
