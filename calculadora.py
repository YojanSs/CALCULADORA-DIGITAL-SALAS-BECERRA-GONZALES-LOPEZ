#calculadora.py # type: ignore

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0: 
        return "Error: No se puede dividir por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return a ** 0.5

while True: #Bucle infinito para mostrar el menú hasta que el usuario decida salir
 print ("Bienvenido Usuario, esta es una calculadora básica")
 print ("opciones:" )
 print ("1.Suma")
 print ("2.Resta")
 print ("3.Multiplicación")
 print ("4.División")
 print ("5.Potencia")
 print ("6.Raíz Cuadrada")
 print ("7.Salir")

 opcion = int(input("Seleccione una opción (1-7):"))
 if opcion == 1:
    num1 = float(input("Ingrese el primer número:"))
    num2 = float(input("Ingrese el segundo número:"))
    resultado = suma (num1, num2)
    print ("El resultado de la suma es:", resultado)


 elif opcion == 2:
    num1 = float(input("Ingrese el primer número:"))
    num2 = float(input("Ingrese el segundo número:"))
    resultado = resta (num1, num2)
    print ("El resultado de la resta es:", resultado)

 elif opcion == 3:
    num1 = float(input("Ingrese el primer número:"))
    num2 = float(input("Ingrese el segundo número:"))
    resultado = multiplicacion (num1, num2)
    print ("El resultado de la multiplicación es:", resultado)

 elif opcion == 4:
    num1 = float(input("Ingrese el primer número:"))
    num2 = float(input("Ingrese el segundo número:"))
    resultado = division (num1, num2)
    print ("El resultado de la división es:", resultado)

 elif opcion == 5:
    num1 = float(input("Ingrese la base:"))
    num2 = float(input("Ingrese el exponente:"))
    resultado = potencia (num1, num2)
    print ("El resultado de la potencia es:", resultado)

 elif opcion == 6:
    num1 = float(input("Ingrese un número para calcular su raíz cuadrada:"))
    resultado = raiz_cuadrada (num1)
    print ("El resultado de la raíz cuadrada es:", resultado)

 elif opcion == 7:
    print ("Gracias por usar la calculadora, Fin de la sesión.")  
    break #Rompe el bucle para salir del programa



