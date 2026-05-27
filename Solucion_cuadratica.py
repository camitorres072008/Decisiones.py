a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a != 0:
    discriminante = (b ** 2) - (4 * a * c)
    
    if discriminante >= 0:
        print("La ecuación TIENE solución real.")
    else:
        print("La ecuación NO TIENE solución real (es imaginaria).")
else:
    print("El valor de a no puede ser 0 para una ecuación cuadrática.")