from tkinter import *
from tkcalendar import *
from tkinter import ttk
from datetime import datetime


def choose_date():
    top = Toplevel()
    cal = Calendar(top, font="Arial 14", selectmode='day', locale='pt_BR',
                   cursor="hand1", year=datetime.now().year,
                   month=datetime.now().month, day=datetime.now().day)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="Selecionar",
               command=lambda: set_date(cal.selection_get())).pack()


def set_date(date):
    date_entry.config(state='normal')
    date_entry.delete(0, END)
    date_entry.insert(0, date.strftime('%d/%m/%Y'))
    date_entry.config(state='readonly')


root = Tk()

date_entry = Entry(root, state='readonly')
date_entry.pack(padx=10, pady=10, side=LEFT, fill=BOTH, expand=True)

button = Button(root, text="...", command=choose_date)
button.place(x=100, y=100)

root.mainloop()
