# Definim la funció
def dividir(a, b):
    """
    Retorna el resultat de a / b. Si b és 0, avisa i retorna None.
    """
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("Error: No es pot dividir per zero!")
        return None

# Proves de la funció
print(dividir(10, 2))   # 5.0
print(dividir(7, 0))    # Error: No es pot dividir per zero! → None
print(dividir(0, 5))    # 0.0