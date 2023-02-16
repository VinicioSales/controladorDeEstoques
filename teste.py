from tkinter import Tk, ttk, Button
from tkcalendar import DateEntry

root = Tk()
style = ttk.Style(root)
style.theme_use('clam')
style.configure('my.DateEntry', foreground='white', background='#3b3b3b', arrowcolor='white', bordercolor='#3b3b3b')
style.configure('my.DateEntry.Calendar', background='#3b3b3b', foreground='white', bordercolor='#3b3b3b')

def print_date():
    date = date_entry.get()
    print(date)

date_entry = DateEntry(root, style='my.DateEntry', borderwidth=2)
date_entry.pack()

print_button = Button(root, text='Print Date', command=print_date)
print_button.pack()

root.mainloop()
