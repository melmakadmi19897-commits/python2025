# Definim la funció
def paraules_per_lletra(llista, lletra):
    """
    Retorna una llista amb les paraules que comencen per la lletra donada.
    """
    return list(filter(lambda paraula: paraula.startswith(lletra), llista))

# Proves de la funció
llista_paraules = ["maria", "manta", "peu", "mà"]
print(paraules_per_lletra(llista_paraules, 'p'))  # ['peu']
print(paraules_per_lletra(llista_paraules, 'm'))  # ['maria', 'manta', 'mà']
print(paraules_per_lletra(llista_paraules, 'x'))  # []