pesop = int (112)
pesom = int (75)
numerop = int (input ("Cuántos payasos se han vendido? "))
numerom = int (input ("Cuántas muñecas se han vendido? "))
pesototal = ((numerop * pesop) + (numerom * pesom))
print("En el último pedido se han vendido un total de ", str (numerop) + " payasos; "
"un total de ", str(numerom) + " muñecas; Y el peso total del pedido es de", str (pesototal) + " gramos")