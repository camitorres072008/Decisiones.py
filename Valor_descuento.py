vlor = float(input("digite el precio del articulo: "))

if vlor >= 150000:
    descuento = vlor * 0.05
else:
    descuento = 0.0

print("su descuento es :", descuento)