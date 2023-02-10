import customtkinter as ctk

janela = ctk.CTk()
progressbar = ctk.CTkProgressBar(master=janela)
progressbar.pack(padx=20, pady=10)
progressbar.configure(mode="indeterminnate")
progressbar.start()

janela.mainloop()