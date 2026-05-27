minimoValor = int(input("Ingrese el valor minimo del intervalo: "))
maximoValor = int(input("Ingrese el valor maximo del intervalo: "))
x = int(input("Ingrese el numero x a verificar: "))

if x >= minimoValor and x <= maximoValor:
    print("El numero", x, "esta DENTRO del intervalo [", minimoValor, ",", maximoValor, "]")
else:
    print("El numero", x, "esta FUERA del intervalo.")