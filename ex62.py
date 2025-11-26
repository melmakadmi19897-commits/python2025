from functools import reduce

# Definim la funció
def Passar_a_Numero(llista):
    """
    Retorna el número que corresponen els dígits de la llista.
    """
    return reduce(lambda x, y: x * 10 + y, llista)

# Proves de la funció
llista1 = [3, 4, 1, 5]
print(Passar_a_Numero(llista1))  # 3415

llista2 = [0, 7, 2]
print(Passar_a_Numero(llista2))  # 72
