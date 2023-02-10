import ast

# String que contém o dicionário
string = "[{'chave1': 'valor1', 'chave2': 'valor2'}]"

# Transforma a string em uma lista
lista = ast.literal_eval(string)

# Imprime a lista
print(type(lista))
for item in lista:
    print(type(item))
    print(item)
