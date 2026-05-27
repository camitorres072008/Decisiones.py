x = int(input("Ingrese un numero entre el 0 y el 20: "))

primos = [2, 3, 5, 7, 11, 13, 17, 19]
if x in primos:
    z = "este es un numero primo "
else:
    z = "este no es un numero primo"

print(z)