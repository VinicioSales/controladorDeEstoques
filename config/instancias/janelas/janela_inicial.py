import customtkinter as ctk

dimensao = "1100x580"

def janela_inicial_func():
    #NOTE - janela_inicio
    """Cria a janela inicial"""
    janela_inicio = ctk.CTk()
    janela_inicio.geometry(dimensao)
    janela_inicio.title("CustomTkinter simple_example.py")
    return janela_inicio
