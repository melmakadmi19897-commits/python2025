# Programa per calcular el capital final amb interès compost

# Funció per demanar un valor dins un rang
def demanar_valor(missatge, minim, maxim):
    while True:
        try:
            valor = float(input(missatge))
            if valor < minim or valor > maxim:
                print(f"El valor ha d'estar entre {minim} i {maxim}. Torna-ho a provar.")
            else:
                return valor
        except ValueError:
            print("Valor invàlid. Torna-ho a provar.")

# Entrada de dades
capital_inicial = demanar_valor("Introdueix la quantitat a sol·licitar (50.000€ - 800.000€): ", 50000, 800000)
interes = demanar_valor("Introdueix l'interès anual (%) (0.5 - 13): ", 0.5, 13)
anys = demanar_valor("Introdueix el número d'anys (3 - 40): ", 3, 40)

# Càlcul del capital final
capital_final = capital_inicial * (1 + interes / 100) ** anys

# Mostrar resultat amb 2 decimals
print(f"\nEl capital final després de {anys:.0f} anys serà: {capital_final:.2f}€")
