#1
for x in range(0,101):
    print(x)

#2
numero = input("Ingrese un número entero: ")

if numero.startswith('-'):
    numero = numero[1:]

cantidad_digitos = len(numero)

print("El número tiene", cantidad_digitos, "dígito(s).")

#3
valorInferior = int(input("Ingresa el valor inferior: "))
valorSuperior = int(input("Ingresa el valor superior: "))

suma = 0
for numero in range(valorInferior + 1, valorSuperior):
    suma += numero

print(f"La suma de los números entre {valorInferior} y {valorSuperior} es: {suma}")

#4
totalAcumulado = 0

while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    totalAcumulado += numero

print(f"El total acumulado es: {totalAcumulado}")

#5
import random

numeroSecreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numeroSecreto:
        break
    print("Incorrecto, intenta de nuevo.")

print(f"¡Correcto! El número era {numeroSecreto}. Lo lograste en {intentos} intento(s).")

#6
for x in range(100,-1, -2):
    print(x)

#7
numeroLimite = int(input("Ingresa un número entero positivo: "))

suma = 0
for numero in range(1, numeroLimite):
    suma += numero

print(f"La suma de los números comprendidos entre 0 y {numeroLimite} es: {suma}")

#8
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#9
suma = 0

for i in range(100):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / 100
print(f"La media de los 100 números ingresados es: {media}")

#10
numero = input("Ingresa un número: ")
numeroInvertido = numero[::-1]
print(f"Número invertido: {numeroInvertido}")


