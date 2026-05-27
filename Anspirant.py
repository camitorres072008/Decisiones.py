genero = input("Género del aspirante (F/M): ").upper()
estadocivil = input("Estado civil del aspirante (S/C/V/D/U): ").upper()

estatura = float(input("Estatura del aspirante (ej: 1.68): "))
edad = int(input("Edad del aspirante: "))

if estadocivil == "S":
    if genero == "F":
        if estatura > 1.60 and 20 <= edad <= 25:
            salida = "Es apto"
        else:
            salida = "No es apto por edad o estatura"
            
    elif genero == "M":
        if estatura > 1.65 and 18 <= edad <= 24:
            salida = "Es apto"
        else:
            salida = "No es apto por edad o estatura"
            
    else:
        salida = "Género no válido"
else:
    salida = "No es apto (Debe ser soltero)"

print(f"Resultado: {salida}")