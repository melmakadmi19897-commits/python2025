# Definim la funció
def crear_repetits(n, caracter):
    """
    Retorna el caràcter multiplicat pel número enter n.
    """
    return caracter * n

# Proves de la funció
print(crear_repetits(5, "a"))     # "aaaaa"
print(crear_repetits(3, "x"))     # "xxx"
print(crear_repetits(0, "b"))     # ""
print(crear_repetits(7, "*"))     # "*******"