pandeayer = int (input ("Cuántas barras se han vendido que no son del día? "))
preciopan = 3.49
descuento = preciopan * 0.60
preciopandeayer = preciopan - descuento 
costetotal = preciopandeayer * pandeayer
print ("Una barra del día cuesta: ", round(preciopan, 2))
print ("El descuento que se la hace a una barra que no es del día es: ", round(descuento, 2))
print ("El coste final de las barras que no son del día es: ", round(costetotal, 2))