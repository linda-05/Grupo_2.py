# EJERCICIO 1:Numero positivo, negativo o cero

# se le solicita al usuario un numero
numero = float(input("Introduce un numero:"))

# se comprueba si es positico, negativo o cero
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")


# EJERCICIO 2:Contador con while

#Se le pide al usuario un numero positivo
numero = int(input("Ingrese un numero positivo:"))

# inicia contador
contador = 1

#contador desde el 1 hasta el numero ingresado
while contador <= numero:
    print(contador)
    contador += 1


#EJERCICIO 3: Tabla de multiplicar con for

#se le pide al usuario un numero
numeros = int(input("Introduce un numero:"))

# mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    resultado = numeros * i
    print(f" {numeros} * {i} = {resultado}")


#EJERCICIO 4: Suma acumulativa con break

#Variable para acumular
suma_total = 0

while True:
    numero = float(input("Ingrese un número (negativo para terminar): "))
    if numero < 0:
        #termina el ciclo si el numero es negativo
        break

    # suma el numero ingresado 
    suma_total += numero

print(f"La suma total es: {suma_total}")