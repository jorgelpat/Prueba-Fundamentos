#Codigo fuente 45 voltajes
cont = 5
con = 0
for i in range(cont):
    vol = int(input("Ingrese un valor de voltaje:"))
    con = con + vol

prom = con/5
    
if prom > 220:
    print("Alto voltaje")
else:
    print("Voltaje correcto")