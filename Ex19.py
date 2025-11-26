def sumar_llista(llista):
    sumar = 0
    for e in llista:
        sumar+=e
    return sumar 
    
def multiplicar_llista(llista):
    multiplicar=1
    for e in llista:
        multiplicar*=e
        return multiplicar
    
# Programa principal
a = [1, 3, 5, 6, 7, 10]
print("La suma dels elemnets de la llista {} val {}".format(a, sumar_llista(a)))
print("La multiplicació dels elements de la llista {} val {}".format(a, multiplicar_llista(a)))
