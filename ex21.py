# Definim la funció
def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari
    """
    # Convertim la paraula a minúscules per ignorar majúscules/minúscules
    paraula = paraula.lower()
    # Comprovem si és igual llegida de dreta a esquerra
    return paraula == paraula[::-1]

# Proves de la funció
print(es_palindrom("radar"))   # True
print(es_palindrom("ara"))     # True
print(es_palindrom("civic"))   # True
print(es_palindrom("rallar"))  # True
print(es_palindrom("tapat"))   # True
print(es_palindrom("simis"))   # True
print(es_palindrom("refer"))   # True
print(es_palindrom("hola"))    # False
print(es_palindrom("Python"))  # False