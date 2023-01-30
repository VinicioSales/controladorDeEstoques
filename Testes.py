from tkinter import *

root = Tk()
root.title("Aumentando a fonte do texto")

texto = StringVar()
texto.set("Texto com fonte grande")

label = Label(root, textvariable=texto, font=("Arial", 10))
label.pack()

root.mainloop()
