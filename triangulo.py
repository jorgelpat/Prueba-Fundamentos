base = float(input("Indique la base: "))
altura = float(input("Indique la altura: "))

area = (base*altura)/2

if area > 1000:
    print("Datos no validos")
else:
    print(f"El area es {area}")