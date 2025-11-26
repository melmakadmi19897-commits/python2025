# Funció per demanar un número dins d'un rang
def demanar_numero(missatge, minim, maxim):
    while True:
        try:
            numero = int(input(missatge))
            if numero < minim or numero > maxim:
                print(f"El número ha d'estar entre {minim} i {maxim}. Torna-ho a provar.")
            else:
                return numero
        except ValueError:
            print("Entrada invàlida. Introdueix un número enter.")

# Programa principal
numero = demanar_numero("Introdueix un número (1 - 900000): ", 1, 900000)

# Comptem la quantitat de dígits
quantitat_digits = len(str(numero))

print(f"El número {numero} té {quantitat_digits} dígits.")