from math import *
from tkinter import *

aken=Tk()
aken.geometry("750x200")
aken.title("Ruudukujulised võrrandid")
lbl=Label(aken,
          text="Kvadraatilise võrrandi lahendamine",
          bg="lightblue",
          fg="green",
          font="Arial 20")
a=Entry(aken,
       fg="blue",
       bg="lightblue",
       width=5,
       font="Arial 20",
       justify=CENTER)
t1=Label(aken,
         text="x**2+",
         fg="green",
         font="Arial 20")
b=Entry(aken, fg="blue",
        bg="lightblue",
        width=5,
        font="Arial 20",
        justify=CENTER)
t2=Label(aken,
         text="x+",
         fg="green",
         font="Arial 20")
c=Entry(aken,
        fg="blue",
        bg="lightblue",
        width=5,
        font="Arial 20",
        justify=CENTER)
t3=Label(aken,
         text="=0",
         fg="green",
         font="Arial 20")
lah=Button(aken,
           text="Lahenda",
          font="Arial 24",
          bg="green",
          relief=GROOVE,
          width=10)
res=Label(aken,
          text="Lahendus",
          bg="yellow",
          font="Arial 10",
          width=50,
          height=3)

res.pack(side=BOTTOM)
lbl.pack()
a.pack(side=LEFT)
t1.pack(side=LEFT)
b.pack(side=LEFT)
t2.pack(side=LEFT)
c.pack(side=LEFT)
t3.pack(side=LEFT)
lah.pack(side=LEFT)
aken.mainloop()