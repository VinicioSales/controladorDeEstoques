import json
import requests
#from config.credenciais.database import database_infos_func
from unidecode import unidecode
from datetime import datetime
import customtkinter as ctk

def sub_janela_relatorio_func(produtos_nao_retornados_text):
    #NOTE - sub_janela_relatorio_func
    """Mostra o relatório de produtos não retornados
    
    params:
        - string: produtos_nao_retornados
        
    return:
        - None"""
    sub_janela_relatorio = ctk.CTkToplevel()
    sub_janela_relatorio.title("Relatório")
    sub_janela_relatorio.state("zoomed")

    #SECTION - Funcoes Sub 
    
    def inicio_func():
        #NOTE - inicio_func
        """
        Função que destrói a janela de relatórios
        """
        sub_janela_relatorio.withdraw()
        #janela_inicio.deiconify()
    def criar_pedido_venda_btn_func():
        #NOTE - criar_pedido_venda_btn_func
        """
        Função que cria um pedido de venda a partir de uma lista de produtos e quantidades.
        """
        
        for linha in quant_diferenca_estoque:
            
            linha = linha.split("|")
            nome_produto = linha[0]
            quantidade_prod = linha[1]
            quantidade_prod = quantidade_prod.replace(" ", "")
            quantidade_prod = quantidade_prod.replace("\n", "")
            #================ TESTE =================#
            codigo_cliente = "5646179802"
            #================ TESTE =================#
            cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_nome_func(nome_produto)
            sub_janela_data_vencimento = sub_janela_data_vencimento_func(codigo_produto, codigo_cliente, cfop, descricao, ncm, unidade, valor_unitario, quantidade_prod)              
            #incluir_pedido_venda(codigo_produto, codigo_cliente, data_previsao, cfop, descricao, ncm ,unidade, valor_unitario, quantidade_prod)
    sub_janela_relatorio.mainloop()
sub_janela_relatorio_func("teste")