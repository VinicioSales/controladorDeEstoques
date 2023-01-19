lista = ["pera", "maça", "banana"]

fruta = "maça"

for index, item in enumerate(lista):
    if item == fruta:
        lista[index] = "Uva"
print(lista)