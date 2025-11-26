# Definim la funció
def gran_llista(llista):
    """
    Retorna el número més gran d'una llista de números.
    """
    if not llista:  # Comprovem si la llista està buida
        return None
    major = llista[0]
    for numero in llista:
        if numero > major:
            major = numero
    return major

# Proves de la funció
print(gran_llista([3, 4, 2, 3, 10]))  # 10
print(gran_llista([-5, -2, -8, -1]))  # -1
print(gran_llista([7]))               # 7
print(gran_llista([]))                # None
