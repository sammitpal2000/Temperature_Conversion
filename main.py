from tkinter import *
root = Tk()
root.title("Temperature Conversion")
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(300,300)

tenter = DoubleVar()
Label(root,text="Temperature Conversion",font="calibri 15 bold").pack()
Entry(root,textvariable=tenter).pack(pady=10)

def convert():
    x = tenter.get()
    t = (x - 32) * 0.55556
    l1.config(text=t)


Button(root,text="Convert",command=convert).pack(pady=10)
l1 = Label(root,text="")
l1.pack()
root.mainloop()
