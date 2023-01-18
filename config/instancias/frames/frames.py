import tkinter
import customtkinter as ctk

def frame_1_inicio_func(janela):
    #NOTE - frame_1_inicio_func
    """Frame 1 da tela inicial
    param: janela
    return: frame_1_inicio"""
    frame_1_inicio = ctk.CTkFrame(master=janela)
    frame_1_inicio.pack(pady=20, padx=60, fill="both", expand=True)
    return frame_1_inicio

def frame_1_sai_func(janela):
    #NOTE - frame_1_sai_func
    """Frame 1 da tela saida de caminhões
    param: janela
    return: frame_1_sai"""
    frame_1_sai = ctk.CTkFrame(master=janela)
    frame_1_sai.pack(pady=20, padx=60, fill="both", expand=True)
    return frame_1_sai