# Definim la funció
def crear_llista_fitxer(nom_fitxer):
    """
    Llegeix un fitxer i retorna una llista amb totes les paraules.
    Cada paraula és un element de la llista.
    """
    llista_paraules = []
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer:
                # Separa les paraules per espais i afegeix a la llista
                paraules = linia.split()
                llista_paraules.extend(paraules)
        return llista_paraules
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return []

# Exemple d'ús
nom_fitxer = "exemple.txt"  # Assegura't que aquest fitxer existeix
llista = crear_llista_fitxer(nom_fitxer)
print("Llista de paraules llegides del fitxer:")
print(llista)
