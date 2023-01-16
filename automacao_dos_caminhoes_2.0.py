import tkinter
import customtkinter as ctk
from config.instancias import frame_1_inicio_func
#from config.instancias import frame_1_sai_func
from config.instancias import janela_saida_caminhoes_func
from config.instancias import janela_inicio_func
from config.styles import estilo_janelas
#from config.instancias.janelas import janela_saida_caminhoes_func


#NOTE - JANELA INICIO
janela_inicio = janela_inicio_func()

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


#SECTION - SAI CAMINHAO
#===================== PAGINA SAIDA CAMINHOES ==================#

#====================== FRAMES ===================#
#frame_1_sai = frame_1_sai_func(janela_sai_caminhoes)

#======= INPUTS =======#
'''texto = ctk.CTkTextbox(master = frame_1_sai, width=250)
texto.insert("0.0", "Preencha os dados:")
entry = ctk.CTkEntry(master=frame_1_sai, placeholder_text="CTkEntry")
entry.grid(row=3, column=1, columnspan=2, padx=(5, 0), pady=(5, 5), sticky="nsew")'''

'''def ajustar_estoque():
    print("Quantidade:", quantidade_var.get())
    print("Valor:", valor_var.get())

app = ctk.CTk()
app.geometry("400x300")

quantidade_var = ctk.StringVar()
valor_var = ctk.StringVar()

quantidade_label = ctk.CTkLabel(master=frame_1_sai, text="Quantidade de itens")
quantidade_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

quantidade_entry = ctk.CTkEntry(master=frame_1_sai, textvariable=quantidade_var)
quantidade_entry.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

valor_entry = ctk.CTkEntry(master=frame_1_sai, textvariable=valor_var)
valor_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

ajustar_estoque_button = ctk.CTkButton(master=frame_1_sai, text="Ajustar Estoque", command=ajustar_estoque)
ajustar_estoque_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)'''

#!SECTION

janela_inicio.mainloop()