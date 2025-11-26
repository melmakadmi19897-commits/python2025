# Definim la funció
def filtrar_paraules(llista_paraules, x):
    """
    Retorna una llista amb les paraules que tenen més de x caràcters.
    """
    return [paraula for paraula in llista_paraules if len(paraula) > x]

# Proves de la funció
paraules = ["Hola", "Ramis", "IES", "Paraula", "Python"]

print(filtrar_paraules(paraules, 4))  # ["Ramis", "Paraula", "Python"]
print(filtrar_paraules(paraules, 5))  # ["Paraula", "Python"]
print(filtrar_paraules(paraules, 7))  # []
print(filtrar_paraules([], 3))        # []