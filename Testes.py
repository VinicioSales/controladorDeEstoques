import tkinter as tk

def on_click(event):
    print("Textbox clicado")

root = tk.Tk()
textbox = tk.Text(root)
textbox.pack()
textbox.bind("<Button-1>", on_click)
root.mainloop()
