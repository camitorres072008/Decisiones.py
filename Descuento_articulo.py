valor = float(input("Ingrese el valor del artículo: "))

tipo = input("Ingrese el tipo de artículo: ")

if tipo == "1":
    porcentaje = 0.125
elif tipo == "2":
    porcentaje = 0.083
elif tipo == "3":
    porcentaje = 0.032
else:
    porcentaje = 0.0

descuento = valor * porcentaje

print("El valor del descuento es:", descuento)