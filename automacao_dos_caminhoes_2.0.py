import tkinter
import customtkinter as ctk
from config.instancias import frame_1_inicio_func
from config.instancias import frame_1_sai_func
from config.instancias import janela_saida_caminhoes_func
from config.styles import estilo_janelas
from config.instancias import janela_inicial_func


#NOTE - JANELA INICIO
janela_inicio = janela_inicial_func()

#SECTION - INICIO
#====================== FRAMES ===================#
frame_1_inicio = frame_1_inicio_func(janela_inicio)

#=============== FUNCAO BOTAO ==================#
def btn_saida_caminhao_func():
    #//NOTE - btn_saida_caminhao_func
    """Abre a janela de saida de caminhões
    """
    
    janela_sai_caminhoes = janela_saida_caminhoes_func()
    #janela_inicio.withdraw()
    janela_inicio.destroy
def btn_entrada_caminhao_func():
    #//NOTE - btn_entrada_caminhao_func
    """Abre a janela de entrada de caminhões
    """
    jan_entrada_caminhao = ctk.CTkToplevel()
    jan_entrada_caminhao.geometry("200x200")
    jan_entrada_caminhao.title("Entrada de caminhão")
    janela_inicio.withdraw()
def btn_produtos_func():
    #//NOTE - btn_produtos_func
    """Abre a janela de produtos
    """
    jan_produtos = ctk.CTkToplevel()
    jan_produtos.geometry("200x200")
    jan_produtos.title("Produtos")
    janela_inicio.withdraw()

#==================== PAGINA INICIAL ================#
#========= BOTOES ===========#
btn_saida_caminhao = ctk.CTkButton(
    master=frame_1_inicio,
    text="Saída de caminhões",
    hover_color = "#AA0",
    command=btn_saida_caminhao_func
)
btn_saida_caminhao.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)

btn_entrada_caminhao = ctk.CTkButton(
    master=frame_1_inicio,
    text="Entrada de caminhões",
    hover_color = "#AA0",
    command=btn_entrada_caminhao_func
)
btn_entrada_caminhao.place(relx=0.3, rely=0.1, anchor=tkinter.CENTER)

btn_produtos = ctk.CTkButton(
    master=frame_1_inicio,
    text="Produtos",
    hover_color = "#AA0",
    command=btn_produtos_func
)
btn_produtos.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
#!SECTION


janela_inicio.mainloop()