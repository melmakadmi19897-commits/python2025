# Programa per sumar els dígits i comprovar si és parell o senar

# Entrada del número
while True:
    try:
        numero = int(input("Introdueix un número enter: "))
        break
    except ValueError:
        print("Entrada invàlida. Introdueix un número enter.")

# Suma dels dígits
suma_digits = sum(int(d) for d in str(abs(numero)))  # abs per evitar problemes amb números negatius

# Comprovació parell/senar
if suma_digits % 2 == 0:
    tipus = "parell"
else:
    tipus = "senar"

# Mostrar resultats
print(f"La suma dels dígits de {numero} és {suma_digits} i és {tipus}.")