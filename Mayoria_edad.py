nombre = input("Ingrese su nombre: ")

edad = int(input("Ingrese su edad: "))


if edad >= 18:
    mensaje = "Mayor de edad "
else:
    mensaje = "menor de edad"

print("Hola", nombre)
print("Usted es", mensaje)