def verificar_type(x):
    if type(x) == int or type(x) == float:
        return True
    else:
        return False

a = verificar_type("2.2")
print(a)