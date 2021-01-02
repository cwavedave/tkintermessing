import tkinter

window = tkinter.Tk()

window.title("GUI Program")
window.minsize(width=720,height=480)
window.maxsize(width=1420, height=1080)

my_label = tkinter.Label(text="Label", font=("Arial",24,"bold"))
my_label.pack()

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1,4,5,10,13,12))






















#Always at end of program
window.mainloop()
