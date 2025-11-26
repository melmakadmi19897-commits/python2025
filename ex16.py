# Definim la funció
def gran_de_tres(a, b, c):
    """
    Retorna el número més gran entre a, b i c
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Proves de la funció
print(gran_de_tres(5, 10, 3))     # Ha de retornar 10
print(gran_de_tres(-2, 0, -5))    # Ha de retornar 0
print(gran_de_tres(7, 7, 7))      # Ha de retornar 7
print(gran_de_tres(12.5, 7.3, 12.7))  # Ha de retornar 12.7