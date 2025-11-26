# Definim la funció
def es_de_traspas(any):
    """
    Retorna True si l'any és de traspàs, False en cas contrari.
    Un any és de traspàs si és divisible per 4 i no per 100,
    o bé és divisible per 400.
    """
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

# Proves de la funció
anys = [2000, 2004, 1900, 2021, 2024]

for any in anys:
    if es_de_traspas(any):
        print(f"{any} és un any de traspàs.")
    else:
        print(f"{any} NO és un any de traspàs.")

