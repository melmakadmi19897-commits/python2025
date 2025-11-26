# Definim la funció
def mostrar_majors_que(tupla, x):
    """
    Imprimeix tots els elements de la tupla que són majors que x.
    """
    for numero in tupla:
        if numero > x:
            print(numero, end=' ')
    print()  # salt de línia final

# Programa principal per provar la funció
# Entrada de valors per a la tupla
valors = input("Introdueix els números enters separats per espais: ")

# Convertim l'entrada a una tupla d'enters
tupla_numeros = tuple(int(num) for num in valors.split())

# Mostrar els números majors de 18
print("Nombres majors de 18:")
mostrar_majors_que(tupla_numeros, 18)