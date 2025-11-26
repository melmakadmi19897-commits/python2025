# Definim la funció
def hi_ha_duplicats(llista):
    """
    Retorna True si hi ha algun element duplicat a la llista,
    False en cas contrari.
    """
    return len(llista) != len(set(llista))

# Proves de la funció
print(hi_ha_duplicats([1, 2, 3, 4]))        # False
print(hi_ha_duplicats([1, 2, 2, 4]))        # True
print(hi_ha_duplicats(["a", "b", "c"]))     # False
print(hi_ha_duplicats(["a", "b", "a"]))     # True
print(hi_ha_duplicats([]))                  # False