#Calculadora Basicas 
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Selecciona la operación (sumar, restar, multiplicar, dividir): ")

if operacion == "sumar":
    print(sumar(num1, num2))
elif operacion == "restar":
    print(restar(num1, num2))
elif operacion == "multiplicar":
    print(multiplicar(num1, num2))
elif operacion == "dividir":
    print(dividir(num1, num2))
else:
    print("Operación no válida.")
