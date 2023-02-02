'''prods_selecionados = [" milho | 20\n", " maca | 30\n", " pera | 40\n"]
prods_ceasa = ["milho | 1\n", "pera | 2\n"]
lista_quant_resultado = []
for prod_selecionado, prod_ceasa in zip(prods_selecionados, prods_ceasa):
    prod_selecionado = prod_selecionado.split("|")
    nome_selecionado = prod_selecionado[0]
    nome_selecionado_aux = nome_selecionado.replace(" ", "")
    prod_ceasa = prod_ceasa.split("|")
    nome_ceasa = prod_ceasa[0]
    nome_ceasa_aux = nome_ceasa.replace(" ", "")
    print(f"nome_ceasa_aux: {nome_ceasa_aux} - nome_selecionado_aux: {nome_selecionado_aux}")
    if nome_ceasa_aux == nome_selecionado_aux:
        quant_selecionado = prod_selecionado[1]
        quant_selecionado = quant_selecionado.replace(" ", "")
        quant_selecionado = int(quant_selecionado.replace("\n", ""))
        quant_ceasa = prod_ceasa[1]
        quant_ceasa = quant_ceasa.replace(" ", "")
        quant_ceasa = int(quant_ceasa.replace("\n", ""))
        quant_resultado = quant_selecionado - quant_ceasa
        lista_quant_resultado.append(f"{nome_selecionado} | {quant_resultado}")
print(f"lista_quant_resultado: {lista_quant_resultado}")'''



prods_selecionados = [" milho | 20\n", " maca | 30\n", " pera | 40\n"]
prods_ceasa = ["milho | 1\n", "pera | 2\n"]
lista_quant_resultado = []
for prod_ceasa in prods_ceasa:
    for prod_selecionado in prods_selecionados:
        
        print(f"prod_selecionado: {prod_selecionado} - prod_ceasa: {prod_ceasa}")
        prod_selecionado = (prod_selecionado).split("|")
        nome_selecionado = prod_selecionado[0]
        nome_selecionado_aux = nome_selecionado.replace(" ", "")
        print(type(prod_ceasa))
        prod_ceasa = prod_ceasa.split("|")
        nome_ceasa = prod_ceasa[0]
        nome_ceasa_aux = nome_ceasa.replace(" ", "")
        print(f"nome_ceasa_aux: {nome_ceasa_aux} - nome_selecionado_aux: {nome_selecionado_aux}")
        if nome_ceasa_aux == nome_selecionado_aux:
            quant_selecionado = prod_selecionado[1]
            quant_selecionado = quant_selecionado.replace(" ", "")
            quant_selecionado = int(quant_selecionado.replace("\n", ""))
            quant_ceasa = prod_ceasa[1]
            quant_ceasa = quant_ceasa.replace(" ", "")
            quant_ceasa = int(quant_ceasa.replace("\n", ""))
            quant_resultado = quant_selecionado - quant_ceasa
            lista_quant_resultado.append(f"{nome_selecionado} | {quant_resultado}")
print(f"lista_quant_resultado: {lista_quant_resultado}")