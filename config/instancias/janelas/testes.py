import tkinter as tk

def hide_window1():
    window1.withdraw()
    window2.deiconify()

def hide_window2():
    window2.withdraw()
    window1.deiconify()

window1 = tk.Tk()
window1.title("Janela 1")

button = tk.Button(window1, text="Esconder", command=hide_window1)
button.pack()

window2 = tk.Tk()
window2.title("Janela 2")
window2.withdraw()

button2 = tk.Button(window2, text="Esconder", command=hide_window2)
button2.pack()

window1.mainloop()
