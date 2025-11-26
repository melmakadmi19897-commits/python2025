# Definim la funció
def eliminarcapicua(llista):
    """
    Retorna una nova llista sense el primer i l'últim element.
    """
    if len(llista) <= 2:  # Si té 2 o menys elements, retornem llista buida
        return []
    return llista[1:-1]

# Proves de la funció
llista1 = [10, 20, 30, 40, 50]
print(eliminarcapicua(llista1))  # [20, 30, 40]

llista2 = ["a", "b", "c", "d"]
print(eliminarcapicua(llista2))  # ['b', 'c']

llista3 = [1, 2]
print(eliminarcapicua(llista3))  # []

llista4 = [5]
print(eliminarcapicua(llista4))  # []
