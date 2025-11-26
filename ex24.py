# Definim la funció
def crear_punts(llista):
    """
    Mostra per pantalla tants punts com el valor de cada número de la llista,
    amb un salt de línia entre cada element.
    """
    for numero in llista:
        print("." * numero)

# Proves de la funció
crear_punts([2, 3, 4])
# Sortida esperada:
# ..
# ...
# ....
