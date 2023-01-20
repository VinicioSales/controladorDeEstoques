#NOTE - Imports
import tkinter
import customtkinter as ctk
from datetime import date
from config.instancias.frames import frame_1_inicio_func
from config.instancias.frames import frame_1_sai_func
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
ctk.set_appearance_mode(tema_janela)

#SECTION - INICIO
#====================== FRAMES ===================#
frame_1_inicio = frame_1_inicio_func(janela_inicio)

#=============== FUNCAO BOTAO ==================#
def btn_saida_caminhao_func():
    #//NOTE - btn_saida_caminhao_func
    """Abre a janela de movimento de estoque
    params:
        - None

    return:
        - None
    """
    
    janela_sai_caminhoes = janela_mov_estoque_func(tipo="SAI")
    #janela_inicio.withdraw()
    janela_inicio.destroy
def btn_entrada_caminhao_func():
    #//NOTE - btn_entrada_caminhao_func
    """Abre a janela de movimento de estoque
    params:
        - None

    return:
        - None
    """
    janela_sai_caminhoes = janela_mov_estoque_func(tipo="ENT")
def btn_relatorio_func():
    #//NOTE - btn_relatorio_func
    """Abre a janela de relatorio de diferença de quantidade
    params:
        - None

    return:
        - None
    """
    janela_relatorio_diferenca = janela_relatorio_diferenca_func()

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

btn_relatorio = ctk.CTkButton(
    master=frame_1_inicio,
    text="Relatório",
    hover_color = "#AA0",
    command=btn_relatorio_func
)
btn_relatorio.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
#!SECTION


janela_inicio.mainloop()