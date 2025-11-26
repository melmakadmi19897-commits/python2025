# Definició de la funció
def gran(a, b):
    """
    Retorna el número més gran entre a i b
    """
    if a > b:
        return a
    else:
        return b

# Proves de la funció amb diferents exemples
print("Gran entre 5 i 10:", gran(5, 10))      # Ha de retornar 10
print("Gran entre 20 i 15:", gran(20, 15))    # Ha de retornar 20
print("Gran entre -3 i -7:", gran(-3, -7))    # Ha de retornar -3
print("Gran entre 7 i 7:", gran(7, 7))        # Ha de retornar 7