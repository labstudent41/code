from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Resume')
root.geometry('600x300')
root.minsize(200, 100)

name = Label(root, text='Name').grid(row=0)
nameE = Entry(root).grid(row=0, column=1)

email = Label(root, text='Email').grid(row=0, column=3)
emailE = Entry(root).grid(row=0, column=4)

age = Label(root, text='Age').grid(row=2)
ageE = Spinbox(root, from_=14, to=110).grid(row=2, column=1)



genderL = Label(root, text='Gender').grid(row=3, column=0)
g = IntVar()
male = Radiobutton(root, text="Male", variable=g,
                      value=1).grid(row=3, column=1)
female = Radiobutton(root, text="Female", variable=g,
                      value=2).grid(row=3, column=2)


qual = Label(root, text='Qualification').grid(row=4, column=0)
ssc = IntVar()
sscB = Checkbutton(root, text="SSC", variable=ssc).grid(row=4, column=1)
hsc = IntVar()
hscB = Checkbutton(root, text="HSC", variable=hsc).grid(row=4, column=2)
diploma = IntVar()
diplomaB = Checkbutton(root, text="Diploma",
                       variable=diploma).grid(row=4, column=3)


state = StringVar()
states = ['Maharashtra', 'Delhi', 'Karnataka', 'Uttar Pradesh',
          'Utrakhand', 'Punjab', 'Haryana', 'Assam', 'Tamil Nadu', 'Goa',
          'Himanchal Pradesh', 'Bihar', 'Andhra Pradesh']
stateL = Label(root, text='State').grid(row=5, column=0)
stateC = Combobox(root, text='Select', textvariable=state,
                  values=states).grid(row=5, column=1)

address = Label(root, text='Address').grid(row=7)
addressE = Text(root, width=40, height=5).grid(row=7, column=1, columnspan=5)

root.mainloop()
