# Definim la funció
def llista_a_diccionari(llista):
    """
    Retorna un diccionari amb els elements de la llista com a claus
    i els seus índexs com a valors.
    """
    return {valor: idx for idx, valor in enumerate(llista)}

# Proves de la funció
llista1 = ['casa', 'cotxe', 'cadira', 'taula']
print(llista_a_diccionari(llista1))
# {'casa': 0, 'cotxe': 1, 'cadira': 2, 'taula': 3}

llista2 = ['Python', 'Java', 'C++']
print(llista_a_diccionari(llista2))
# {'Python': 0, 'Java': 1, 'C++': 2}
