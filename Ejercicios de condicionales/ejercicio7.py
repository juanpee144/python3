renta = int (input("Cuál es tu renta anual?: "))
tipoimpositivo = 0

if renta < 10000:
    tipoimpositivo += 5
    print ("Tu tipo impositivo es: ", tipoimpositivo)
elif renta >= 10000 and renta < 20000:
    tipoimpositivo += 15
    print ("Tu tipo impositivo es: ", tipoimpositivo)
elif renta >= 20000 and renta < 35000:
    tipoimpositivo += 20
    print ("Tu tipo impositivo es: ", tipoimpositivo)
elif renta >= 35000 and renta < 60000:
    tipoimpositivo += 30
    print ("Tu tipo impositivo es: ", tipoimpositivo)
elif renta >= 60000:
    tipoimpositivo += 45
    print ("Tu tipo impositivo es: ", tipoimpositivo)