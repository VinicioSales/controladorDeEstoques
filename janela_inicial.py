#NOTE - Imports
import tkinter
import customtkinter as ctk
from datetime import date
from config.instancias import janela_inicial_func
from config.instancias import janela_mov_estoque_func
from config.instancias import janela_relatorio_diferenca_func
from config.styles.styles import estilo_janelas_func
from config.instancias.apis import listar_local_estoque
from config.instancias.apis import listar_projetos
from config.instancias.apis import listar_produtos

#SECTION - Puxando listas
#NOTE - listar_local_estoque
data_atual = date.today()
data_atual = data_atual.strftime("%d/%m/%Y")
with open("config/arquivos/data_anterior.txt", "r") as arquivo:
    data_anterior = arquivo.read()
    
if str(data_atual) != str(data_anterior):
    with open("config/arquivos/lista_produtos_ceasa.txt", "w") as arquivo:
        arquivo.write("")
    with open("config/arquivos/produtos_venda.txt", "w") as arquivo:
        arquivo.write("")
    with open("config/arquivos/lista_pedidos_venda.txt", "w") as arquivo:
        arquivo.write("")

with open("config/arquivos/data_anterior.txt", "w") as arquivo:
    arquivo.write(data_atual)

lista_estoque = listar_local_estoque()
with open(f"config/arquivos/lista_estoques.txt", "r") as arquivo:
    lista_estoques_arquivo = arquivo.readlines()
lista_estoques_arquivo = []
for item in lista_estoque:
    lista_estoques_arquivo.append(f"{item}\n")
with open("config/arquivos/lista_estoques.txt", "w") as arquivo:
    arquivo.writelines(lista_estoques_arquivo)

#NOTE - listar_projetos
lista_projetos = listar_projetos()
with open(f"config/arquivos/lista_projetos.txt", "r") as arquivo:
    lista_projetos_arquivo = arquivo.readlines()
lista_projetos_arquivo = []
for item in lista_projetos:
    lista_projetos_arquivo.append(f"{item}\n")
with open("config/arquivos/lista_projetos.txt", "w") as arquivo:
    arquivo.writelines(lista_projetos_arquivo)

lista_produtos = listar_produtos()
with open(f"config/arquivos/lista_produtos.txt", "r") as arquivo:
    lista_produtos_arquivo = arquivo.readlines()
lista_produtos_arquivo = []
for item in lista_produtos:
    lista_produtos_arquivo.append(f"{item}\n")
with open("config/arquivos/lista_produtos.txt", "w") as arquivo:
    arquivo.writelines(lista_produtos_arquivo)
#!SECTION

#NOTE - JANELA INICIO
janela_inicio = janela_inicial_func()   
estilo_janelas = estilo_janelas_func()
tema_janela = estilo_janelas["tema_janela"]
janela_inicio.state("zoomed")
ctk.set_appearance_mode(tema_janela)

#SECTION - INICIO
#====================== FRAMES ===================#

frame_1_inicio = ctk.CTkFrame(
    master=janela_inicio,
    width=500,
    height=500
    )
frame_1_inicio.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
prods_selecionados = ""

#=============== FUNCAO BOTAO ==================#
quant_produtos_ceasa = ""
prods_ceasa = ""
def btn_saida_caminhao_func():
    #//NOTE - btn_mov_estoque_func
    """Abre a janela de movimento de estoque
    params:
        - None

    return:
        - None
    """
    #janela_inicio.withdraw()
    janela_sai_caminhoes = janela_mov_estoque_func(janela_inicio, prods_selecionados, "SAI", prods_ceasa)
def btn_entrada_caminhao_func():
    #//NOTE - btn_entrada_caminhao_func
    """Abre a janela de movimento de estoque
    params:
        - None

    return:
        - None
    """
    janela_sai_caminhoes = janela_mov_estoque_func(janela_inicio, prods_selecionados, "ENT", prods_ceasa)
def btn_relatorio_func():
    #//NOTE - btn_relatorio_func
    """Abre a janela de relatorio de diferença de quantidade
    params:
        - None

    return:
        - None
    """
    #janela_inicio.withdraw()
    janela_relatorio_diferenca = janela_relatorio_diferenca_func(janela_inicio)

#==================== PAGINA INICIAL ================#
#========= BOTOES ===========#
btn_sai_estoque = ctk.CTkButton(
    master=frame_1_inicio,
    text="Saída de estoque",
    hover_color = "#AA0",
    width=200,
    height=50,
    font=("Arial", 20, "bold"),
    command=btn_saida_caminhao_func
)
btn_sai_estoque.place(relx=0.5, rely=0.39, anchor=tkinter.CENTER)

btn_ent_estoque = ctk.CTkButton(
    master=frame_1_inicio,
    text="Entrada de estoque",
    hover_color = "#AA0",
    width=200,
    height=50,
    font=("Arial", 20, "bold"),
    command=btn_entrada_caminhao_func
)
btn_ent_estoque.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

btn_relatorio = ctk.CTkButton(
    master=frame_1_inicio,
    text="Relatório",
    font=("Arial", 20, "bold"),
    hover_color = "#AA0",
    command=btn_relatorio_func
)
btn_relatorio.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
#!SECTION

janela_inicio.mainloop()