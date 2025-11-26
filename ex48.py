# Definim la funció
def esta_ordenada(llista):
    """
    Comprova si una llista de números està ordenada.
    Retorna un missatge indicant l'ordre.
    """
    if llista == sorted(llista):
        return "Està ordenada de forma ascendent."
    elif llista == sorted(llista, reverse=True):
        return "Està ordenada de forma descendent."
    else:
        return "No està ordenada."

# Proves de la funció
print(esta_ordenada([3, 2, 1]))      # Està ordenada de forma descendent.
print(esta_ordenada([4, 5, 6]))      # Està ordenada de forma ascendent.
print(esta_ordenada([1, 3, 2, 4]))   # No està ordenada.
print(esta_ordenada([7]))            # Està ordenada de forma ascendent (per tractar llista d'un element com ascendent)
print(esta_ordenada([]))             # Està ordenada de forma ascendent (llista buida considerada ordenada)
