sexo = input ("Cuál es tu sexo?: ").lower()
nombre = input ("Cuál es tu nombre?: ").lower()

if sexo == "mujer" and nombre <= "m":
    print ("Eres del grupo A")
elif sexo == "hombre" and nombre >= "n":
    print ("Eres del grupo A")
else:  print ("Eres del grupo B")