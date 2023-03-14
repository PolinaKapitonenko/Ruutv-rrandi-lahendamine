from math import *
from tkinter import *

aken=Tk()
aken.geometry("750x200")
aken.title("Ruudukujulised võrrandid")
lbl=Label(aken,
          text="Решение квадратного уровнения",
          bg="lightblue",
          fg="green",
          font="Arial 25")
a=Entry(aken,
       fg="blue",
       bg="blue",
       width=5,
       font="Arial 25",
       justify=CENTER)
tabel1=Label(aken,
         text="x**2+",
         fg="green",
         font="Arial 25")
b=Entry(aken, fg="blue",
        bg="blue",
        width=5,
        font="Arial 25",
        justify=CENTER)
tabel2=Label(aken,
         text="x+",
         fg="green",
         font="Arial 20")
c=Entry(aken,
        fg="blue",
        bg="blue",
        width=5,
        font="Arial 20",
        justify=CENTER)
tabel3=Label(aken,
         text="=0",
         fg="green",
         font="Arial 20")
otsustama=Button(aken,
           text="Решить",
          font="Arial 24",
          bg="green",
          relief=GROOVE,
          width=10)
lahendus=Label(aken,
          text="Решение",
          bg="yellow",
          font="Arial 10",
          width=50,
          height=3)

otsustama.pack(side=BOTTOM)
lbl.pack()
a.pack(side=LEFT)
tabel1.pack(side=LEFT)
b.pack(side=LEFT)
tabel2.pack(side=LEFT)
c.pack(side=LEFT)
tabel3.pack(side=LEFT)
lahendus.pack(side=LEFT)
aken.mainloop()