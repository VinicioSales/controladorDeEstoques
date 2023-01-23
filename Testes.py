import customtkinter as ctk
import tkinter

janela = ctk.CTk()
janela.geometry("800x600")
master = janela

lista = ["a","b","c"]
estoques_text = ctk.CTkTextbox(
    master,
    width=200,
    height=25
    )
combo_lista = ctk.CTkComboBox(master=master, values=lista)
combo_lista.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
estoques_text.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
estoques_text.insert("0.0", "Estoque interno:")
janela.mainloop()