pizzavegana = ("pimiento y tofu")
pizzanovegana = ("peperoni, jamón y salmón")
pedido = input ("Quieres la pizza vegana?: ").lower()

if pedido == "si":
    print("La pizza vegana lleva: ", pizzavegana)
elif pedido == "no":
    print ("La pizza no vegana lleva: ", pizzanovegana)

if pedido == "si":
   extra = input("Qué ingrediente vas a querer?: ").lower()
   print ("Tu pizza vegana llevará tomate, mozzarella y", extra)

elif pedido == "no":
    extra = input("Qué ingrediente vas a querer?: ").lower()
    print ("Tu pizza no vegana llevará tomate, mozzarella y", extra)