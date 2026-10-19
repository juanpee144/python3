edad = int (input ("Cuál es tu edad?: "))
ingresos = int (input ("Cuáles son tus ingresos?: "))
if edad >= 16 and ingresos >= 1000:
    print("Tienes que tributar")
else:
    print ("No tienes que tributar")