import tkinter as tk
from tkinter import ttk
import time

def process_task():
    for i in range(101):
        progress.set(i)
        time.sleep(0.1)

def start_process():
    btn.config(state='disabled')
    process_task()
    btn.config(state='normal')

root = tk.Tk()
root.title("Barra de Progresso")

progress = tk.IntVar()

btn = tk.Button(root, text="Iniciar Processo", command=start_process)
btn.pack()

tk.ttk.Progressbar(root, variable=progress, maximum=100).pack()

root.mainloop()
