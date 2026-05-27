print("por favor ingrese el nivel de agua en el que se encuentra el tanque en este momento")
nivel = int(input())

if 250 < nivel < 450:
    print("debes cerrar la llave ya que el nivel de agua se encuentra en el nivel optimo")
else:
    print("debes abrir la llave ya que el tanque no esta en el rango del nivel optimo")