# Definim la funció
def index_paraula(llista, paraula):
    """
    Retorna l'índex de la paraula en la llista ordenada.
    Retorna -1 si no es troba.
    """
    try:
        return llista.index(paraula)
    except ValueError:
        return -1

# Proves de la funció
llista_paraules = ["apple", "banana", "cherry", "date", "fig"]
print(index_paraula(llista_paraules, "cherry"))  # 2
print(index_paraula(llista_paraules, "orange"))  # -1
print(index_paraula(llista_paraules, "apple"))   # 0
