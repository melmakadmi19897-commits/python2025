# Definim la funció
def coinciden_valor_index(llista):
    """
    Retorna el nombre d'elements on el valor coincideix amb l'índex.
    """
    return sum(1 for idx, valor in enumerate(llista) if idx == valor)

# Proves de la funció
llista1 = [0, 2, 3, 3, 4]
print(coinciden_valor_index(llista1))  # 3 (0, 3, 4)

llista2 = [0, 1, 2, 3, 4]
print(coinciden_valor_index(llista2))  # 5

llista3 = [5, 6, 7]
print(coinciden_valor_index(llista3))  # 0