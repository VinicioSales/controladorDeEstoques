import customtkinter as ctk
from config.styles import estilo_janelas_func

estilo_janela = estilo_janelas_func()
dimensao = estilo_janela["dimensao"]

def janela_inicial_func():
    #NOTE - janela_inicio
    """Cria a janela inicial"""
    janela_inicio = ctk.CTk()
    janela_inicio.geometry(dimensao)
    janela_inicio.title("Início")
    janela_inicio._set_appearance_mode("dark")
    return janela_inicio
