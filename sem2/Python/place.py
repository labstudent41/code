from tkinter import *

root = Tk()
root.geometry('250x150')

name = Label(root, text="Name").place(x=30, y=30)
email = Label(root, text="Email").place(x=30, y=60)
passwd = Label(root, text="Password").place(x=30, y=90)

e1 = Entry(root).place(x=100, y=30)
e1 = Entry(root).place(x=100, y=60)
e1 = Entry(root).place(x=100, y=90)

root.mainloop()
