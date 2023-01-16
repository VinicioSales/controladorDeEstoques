import tkinter
import customtkinter as ctk

dimensao = "1100x580"

def janela_inicio_func():
    #NOTE - janela_inicio
    """Cria a janela inicial"""
    janela_inicio = ctk.CTk()
    janela_inicio.geometry(dimensao)
    janela_inicio.title("CustomTkinter simple_example.py")

    return janela_inicio

'''def janela_saida_caminhoes_func():
    #NOTE - janela_saia_caminhoes
    """Cria a janela de saída de caminhões"""
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    janela_saida_caminhao.title("Saída de caminhão")

    return janela_saida_caminhao'''

def janela_saida_caminhoes_func():
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    fechar_button = ctk.CTkButton(janela_saida_caminhao, text="Fechar", command=janela_saida_caminhao.destroy)
    fechar_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    #janela_saida_caminhao.mainloop()