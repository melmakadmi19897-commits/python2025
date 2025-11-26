# Programa per sumar tots els números entre dos nombres

# Entrada de números
while True:
    try:
        num1 = int(input("Introdueix el primer número: "))
        num2 = int(input("Introdueix el segon número: "))
        break
    except ValueError:
        print("Entrada invàlida. Torna-ho a provar amb nombres enters.")

# Determinar el rang correcte
inici = min(num1, num2)
fi = max(num1, num2)

# Calcular la suma
suma = sum(range(inici, fi + 1))

# Mostrar resultat
print(f"La suma dels números entre {num1} i {num2} (incloent-los) és: {suma}")