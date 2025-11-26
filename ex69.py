# Funció per generar els primers 10 números elevats a una potència donada
def numeros_a_potencia(potencia):
    """
    Retorna una llista amb els números del 0 al 9 elevats a la potència indicada.
    """
    return [i**potencia for i in range(10)]

# Proves de la funció
print(numeros_a_potencia(2))  # Quadrats: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(numeros_a_potencia(3))  # Cubs: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(numeros_a_potencia(4))  # Quartes potències: [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]
