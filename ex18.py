# Definim la funció
def es_vocal(caracter):
    """
    Retorna True si el caràcter és una vocal, False en cas contrari
    """
    vocales = "aeiouAEIOU"
    if len(caracter) != 1:
        return False  # Només admet un caràcter
    return caracter in vocales

# Proves de la funció
print(es_vocal("a"))   # True
print(es_vocal("E"))   # True
print(es_vocal("b"))   # False
print(es_vocal("z"))   # False
print(es_vocal("ae"))  # False, més d'un caràcter

