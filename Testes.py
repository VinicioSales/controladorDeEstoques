import customtkinter as ctk

def abrir_janela():
    janela_filha = ctk.CTk()
    janela_filha.geometry("400x300")
    fechar_button = ctk.CTkButton(janela_filha, text="Fechar", command=janela_filha.destroy)
    fechar_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    janela_filha.mainloop()
    app.iconify()

app = ctk.CTk()
app.geometry("400x300")

abrir_button = ctk.CTkButton(app, text="Abrir Janela", command=abrir_janela)
abrir_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
