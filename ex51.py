# Definim la funció
def elimina_duplicats(llista):
    """
    Retorna una nova llista sense elements duplicats,
    mantenint l'ordre dels elements originals.
    """
    llista_nova = []
    for element in llista:
        if element not in llista_nova:
            llista_nova.append(element)
    return llista_nova

# Proves de la funció
llista1 = [1, 2, 2, 3, 4, 4, 5]
print(elimina_duplicats(llista1))  # [1, 2, 3, 4, 5]

llista2 = ["a", "b", "a", "c", "b"]
print(elimina_duplicats(llista2))  # ['a', 'b', 'c']

llista3 = [10, 20, 30]
print(elimina_duplicats(llista3))  # [10, 20, 30]