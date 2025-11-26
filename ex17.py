# Definim la funció
def longitud(element):
    """
    Retorna la longitud d'una llista o d'una cadena
    """
    comptador = 0
    for _ in element:
        comptador += 1
    return comptador

# Proves de la funció
print(longitud([1, 2, 3, 4, 5]))        # Ha de retornar 5
print(longitud([]))                      # Ha de retornar 0
print(longitud("Hola món"))              # Ha de retornar 8
print(longitud(["a", "b", "c"]))         # Ha de retornar 3
print(longitud(""))                       # Ha de retornar 0
