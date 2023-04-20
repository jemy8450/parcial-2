# "parcial 2"
#En este código, utilizamos un bucle while para pedir al usuario un número entero positivo. Si el usuario introduce un valor incorrecto, se le pide que lo introduzca de nuevo. Una vez que se ha introducido el valor correcto, se utiliza un bucle for para calcular la suma de la serie dada y se imprime el resultado.

while True:
    try:
        N = int(input("Introduce un número entero positivo: "))
        if N > 0:
            break
        else:
            print("Debes introducir un número entero positivo")
    except ValueError:
        print("Debes introducir un número entero positivo")
        
resultado = 0

for i in range(1, N+1):
    resultado += 1/i
    
print("El resultado de la serie es:", resultado)
