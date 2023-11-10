nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")
datos_usuario = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
mensaje = f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}."
print(mensaje)