puntos = float(input("Cuál es tu puntuación?: "))

if puntos < 0.1:
    print ("Tu nivel de rendimiento es inaceptable y tu dinero recibido es 0")
elif puntos >= 0.4 and puntos < 0.6:
    print ("Tu nivel de rendimiento es aceptable y tu dinero recibido es: ", 2400 * 0.4)
elif puntos >= 0.6:
    print ("Tu nivel de rendimiento es meritorio y tu dinero recibido es: ", 2400 * 0.6)