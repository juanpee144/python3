peso = float (input ("Dime tu peso: "))
estatura = float (input ("Dime tu estatura en centímetros: "))
resultado = peso / ((estatura / 100) ** 2)
print ("Tu índice de masa corporal es: " , round (resultado, 2))