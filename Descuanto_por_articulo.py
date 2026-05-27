precio = float(input("Ingrese el precio del artículo: "))

print("Seleccione el tipo de artículo:")
print("1. Textil")
print("2. Electrodoméstico")
print("3. Elementos de cocina")
print("4. Video juego")

tipo = int(input("Opción: "))

if tipo == 1:
    descuento = 0.0
elif tipo == 2:
    descuento = precio * 0.037
elif tipo == 3:
    descuento = precio * 0.042
elif tipo == 4:
    descuento = precio * 0.078
else:
    print("Opción no válida")
    descuento = 0.0

total = precio - descuento

print(f"El valor del descuento es: ${descuento:.2f}")
print(f"El valor total a pagar es: ${total:.2f}")