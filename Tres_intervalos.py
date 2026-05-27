print("Intervalo 1:")
a1 = int(input("  Ingrese el inicio: "))
b1 = int(input("  Ingrese el fin: "))

print("Intervalo 2:")
a2 = int(input("  Ingrese el inicio: "))
b2 = int(input("  Ingrese el fin: "))

print("Intervalo 3:")
a3 = int(input("  Ingrese el inicio: "))
b3 = int(input("  Ingrese el fin: "))

x = int(input("Ingrese el numero x a verificar: "))

if (a1 < x < b1) or (a2 < x < b2) or (a3 < x < b3):
    print("El numero", x, "esta DENTRO de uno de los intervalos.")
else:
    print("El numero", x, "esta FUERA de los tres intervalos.")