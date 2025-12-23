num1 = float(input("Ingresa el primer número: "))
op = input("Ingresa el operador (+, -, *, /)")
num2 = float(input("Ingresa el segundo número: "))

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Error. División entre cero")
        resultado = None
    else:
        resultado = num1 / num2
else:
    print("Operador no válido")
    resultado = None
if resultado is not None:
    print("Resultado:", resultado)
