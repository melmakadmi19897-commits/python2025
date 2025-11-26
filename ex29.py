# Definim la funció
def compta_majuscules(cadena):
    """
    Retorna el nombre de lletres majúscules en la cadena donada.
    """
    comptador = 0
    for car in cadena:
        if car.isupper():
            comptador += 1
    return comptador

# Proves de la funció
print(compta_majuscules("Hola Món"))           # 2 (H i M)
print(compta_majuscules("PYTHON és genial"))   # 6 (P,Y,T,H,O,N)
print(compta_majuscules("aquest és un test"))  # 0
print(compta_majuscules(""))                   # 0
print(compta_majuscules("123 ABC xyz"))        # 3 (A,B,C)

