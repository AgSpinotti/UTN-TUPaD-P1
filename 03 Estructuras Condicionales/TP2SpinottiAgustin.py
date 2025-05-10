#1
edad= int(input('Inrese su edad:'))

if edad >= 18:
    print('Es mayor de edad')
else: print('Es menor de edad')

#2 
nota=float(input('Ingrese su nota:'))

if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

#3
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#4
edad=int(input('Ingrese su edad:'))

if edad < 12:
    print('Es meno de edad')
elif edad >= 12 and edad < 18:
    print('Adolescente')
elif edad >= 18 and edad < 30:
    print('Adulto joven')
else:
    print('Adulto')

#5
contraseña = input('Ingrese una contraseña de entre 8 o 14 caracteres: ')

if len(contraseña) == 8 or len(contraseña)==14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')

#6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

la_moda = mode(numeros_aleatorios)
la_mediana = median(numeros_aleatorios)
la_media = mean(numeros_aleatorios)

print(f"Moda: {la_moda}")
print(f"Mediana: {la_mediana}")
print(f"Media: {la_media:.2f}")

if la_media > la_mediana and la_mediana > la_moda:
    print("Sesgo positivo o a la derecha")
elif la_media < la_mediana and la_mediana < la_moda:
    print("Sesgo negativo o a la izquierda")
elif la_media == la_mediana == la_moda:
    print("Sin sesgo")
else:
    print("No se puede determinar claramente el sesgo")

#7
texto=input('Ingrese una palabra:')
if texto.endswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
    print(texto + '!')

#8
nombre= input('Ingrese su nombre:')
opcion= input('Elige una opción(1: mayúscula, 2: minúscula, 3: primer letra mayúscula ): ')

if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
elif opcion == '3':
    print(nombre.title())

#9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    print("Fecha inválida.")
    exit()

if hemisferio == "N":
    print("Estás en", estacion_norte)
elif hemisferio == "S":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio inválido.")






