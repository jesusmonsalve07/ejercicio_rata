"Programa para saber en que año es mayor la poblacion a es mayor que la del b"

print("""----------------------------------------------""")
print("""--------crecimiento de poblacion--------------""")
print("""----------------------------------------------""")

#input

n = int(1980)
a = float(3.5)
b = float(5)

#processing

while a < b:
    n = n + 1 
    a = a + (a*0.07) 
    b = b + (b*0.05) 

#output

print("En el año ", str(n) , "la ciudad a tendra una poblacion de", str(a), "millones de personas", " y la ciudad b una poblacion de ", str(b), "millones de personas") 