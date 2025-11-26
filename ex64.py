# Definim la funció
def concatena_llistes(llista1, llista2, connector):
    """
    Concatena els elements corresponents de dues llistes amb un connector.
    Retorna una nova llista.
    """
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Proves de la funció
llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
print(concatena_llistes(llista1, llista2, '-'))  # ['sub-campió', 'supra-campiona']

# Exemple amb un altre connector
print(concatena_llistes(llista1, llista2, ' '))  # ['sub campió', 'supra campiona']