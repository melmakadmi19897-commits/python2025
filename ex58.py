# Definim la funció
def elements_parells(llista):
    """
    Mostra els elements de la llista que estan en posicions parells.
    """
    for i in range(0, len(llista), 2):  # Posicions 0, 2, 4, ...
        print(llista[i])

# Proves de la funció
llista_paraules = ["Hola", "món", "Python", "és", "genial", "!"]
print("Elements en posicions parells:")
elements_parells(llista_paraules)
