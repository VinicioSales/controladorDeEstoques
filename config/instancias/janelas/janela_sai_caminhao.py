import customtkinter as ctk

dimensao = "1100x580"

def janela_saida_caminhoes_func():
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    fechar_button = ctk.CTkButton(janela_saida_caminhao, text="Fechar", command=janela_saida_caminhao.destroy)
    fechar_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    janela_saida_caminhao.mainloop()