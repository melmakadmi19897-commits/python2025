opcio=int(input("""Eligeix una opció:
                1. Suma
                2. Resta
                3.Multiplicació
                4. Divisió 
                5. Sortir
                """))
a = int(input("Escriure el primer operand: "))
b = int(input("Escriure el segon operand: "))
if opcio==1:
    print("La suma de {} + {} és {}".format(a, b, a+b))
elif opcio==2: