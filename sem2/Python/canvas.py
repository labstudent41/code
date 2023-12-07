from tkinter import *

root = Tk()

C = Canvas(root, bg="black", height=500, width=600)

x1 = 100
y1 = 100
x2 = 400
y2 = 400

oval = C.create_oval(x1, y1, x2, y2, fill="red")

# centre of circle
Ox = x1 + ((x2 - x1) / 2)
Oy = y1 + ((y2 - y1) / 2)

# point A on circumfrence of circle
Ax = x2
Ay = y1 + ((y2 - y1) / 2)

print(Ox, Oy, Ax, Ay)
line = C.create_line(Ox, Oy, Ax, Ay, fill="green")

arc = C.create_arc(x1, y1, x2, y2, start=50, extent=90, fill="blue")

polygon = C.create_polygon(x1, y1, x1+100, y1+100, x2, y2, x2+100, y2+100, fill="yellow")

C.pack()
mainloop()
