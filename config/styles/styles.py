import tkinter
import customtkinter as ctk

def estilo_janelas_func():
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    estilo_janelas = {
        "tema_janela": "dark",
        "dimensao": "1100x580"
        }
    return estilo_janelas
    