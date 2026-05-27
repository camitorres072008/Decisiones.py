n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
n4 = int(input("Ingrese el cuarto número: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print(n1)
elif n2 > n1 and n2 > n3 and n2 > n4:
    print(n2)
elif n3 > n1 and n3 > n2 and n3 > n4:
    print(n3)
else:
    print(n4)