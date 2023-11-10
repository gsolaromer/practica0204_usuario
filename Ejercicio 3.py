precios_productos = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad de unidades: "))
if producto in precios_productos:
    precio_total = precios_productos[producto] * cantidad
    print(f"El precio de {cantidad} unidades de {producto} es: {precio_total:.2f} euros.")
else:
    print(f"Lo siento, el producto {producto} no está en el diccionario.")