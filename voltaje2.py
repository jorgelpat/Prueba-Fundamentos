cont = 3
con = 0
dif = 0


for i in range(cont):
    vol = int(input("Ingrese un valor de voltaje:"))
    con = con + vol
prom = con/3

if prom <= 115:
    print("Voltaje Correcto")
elif prom > 115 and prom < 220:
    print("Alto Voltaje")
else:
    print("PELIGRO")

