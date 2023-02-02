prods_selecionados = ["milho | 20\n", "maca | 30\n", "pera | 40\n", "abacate | 54\n", "goiaba | 78\n"]
prods_ceasa = ["milho | 1\n", "pera | 2\n", "goiaba | 50"]

lista_quant_resultado = []
for produto in prods_selecionados:
    nome, quant_selecionado = produto.split(" | ")
    quant_selecionado = int(quant_selecionado.strip())
    for produto_ceasa in prods_ceasa:
        nome_ceasa, quant_ceasa = produto_ceasa.split(" | ")
        quant_ceasa = int(quant_ceasa.strip())
        if nome == nome_ceasa:
            resultado = quant_selecionado - quant_ceasa
            lista_quant_resultado.append(f"{nome} | {resultado}")
            break

print(lista_quant_resultado)
