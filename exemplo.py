import customtkinter, tkinter

app = customtkinter.CTk()
app.state("zoomed")

progressbar_1 = customtkinter.CTkProgressBar(app)
progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
progressbar_1.configure(mode="indeterminnate")
progressbar_1.start()

app.mainloop()