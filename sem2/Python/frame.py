from tkinter import *
root = Tk()
root.geometry('800x400')
root.title('Frames')

q1 = Frame(root)
l1 = Label(q1, text="First quadrant").pack()
q1.place(x=400, y=100)

q2 = Frame(root)
l2 = Label(q2, text="Second quadrant").pack()
q2.place(x=100, y=100)

q3 = Frame(root)
l3 = Label(q3, text="Third quadrant").pack()
q3.place(x=100, y=200)

q4 = Frame(root)
l4 = Label(q4, text="Fourth quadrant").pack()
q4.place(x=400, y=200)

root.mainloop()
