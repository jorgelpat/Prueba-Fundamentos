#Codigo fuente 45 voltajes
cont = 5
con = 0
vol = []
prom = con/5
for i in range(cont):
    vol[i] = int(input("Ingrese un valor de voltaje:"))
    con = con + vol[i]
    if prom > 220:
        print("Alto voltaje")
    else:
        print("Voltaje correcto")