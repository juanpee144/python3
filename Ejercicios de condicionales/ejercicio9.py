edad = int (input ("Cuál es tu edad?: "))
if edad < 4:
    print("El precio de la entrada es gratis")
elif edad >= 4 and edad <= 18:
    print ("El precio de la entrada es 5€")
elif edad > 18:
    print ("El precio de la entrada es 10€")