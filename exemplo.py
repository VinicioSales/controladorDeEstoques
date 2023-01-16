import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Main Window")

# Create button
def open_new_window():
    # Create new window
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text="This is a new window.")
    label.pack()
    
button = tk.Button(root, text="Open new window", command=open_new_window)
button.pack()

root.mainloop()