nota1 = float(input("Ingrese la nota del trabajo 1: "))
nota2 = float(input("Ingrese la nota del trabajo 2: "))
nota3 = float(input("Ingrese la nota del trabajo 3: "))
nota4 = float(input("Ingrese la nota del trabajo 4: "))
nota5 = float(input("Ingrese la nota del trabajo 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Su nota definitiva es: ", promedio)
if promedio > 3.5:
    print("Felicidades, usted GANÓ el curso.")
else:
    print("Lo siento, usted PERDIÓ el curso.")