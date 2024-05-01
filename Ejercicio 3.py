productos = {"pan":"1.40","huevos":"2.30","cebolla":"0.85","aceite":"4.35",}

opcion = str(input("Que producto deseas comprar?\n"))
opcion = opcion.lower()

if opcion in productos:
    kilos = float(input("Cuantos kilos deseas llevar?\n"))
    precio = kilos*(float(productos[opcion]))
    print("El precio es: $" + str(precio))
else:
    print("Lo sentimos ese producto no esta en el inventario :(")