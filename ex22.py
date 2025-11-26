def superposicio(llista1, llista2):
    """
    Retorna True si hi ha algun element en comú entre llista1 i llista2,
    False en cas contrari.
    """
    # Convertim les llistes a conjunts i comprovem la intersecció
    return bool(set(llista1) & set(llista2))

# Proves de la funció
print(superposicio([1, 2, 3], [4, 5, 6]))       # False
print(superposicio([1, 2, 3], [3, 4, 5]))       # True
print(superposicio(["a", "b"], ["c", "d"]))     # False
print(superposicio(["a", "b"], ["b", "c"]))     # True
print(superposicio([], [1, 2, 3]))              # False
