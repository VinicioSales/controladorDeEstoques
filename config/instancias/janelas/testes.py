lista = ["a", "", "b"]
for i, item in enumerate(lista):
    if item == "":
        lista.pop(i)
print(lista)