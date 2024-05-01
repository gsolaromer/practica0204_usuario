informacion = {}
bandera = 1
while bandera == 1:
    dato = str(input("Que informacion vas a agregar?(nombre, edad, sexo, teléfono, correo electrónico, etc.)\n"))
    dato = dato.lower()
    valor = str(input("Escribe el dato:\n"))

    informacion[dato] = valor

    print(informacion)

    print("Quieres seguir ejecutando el programa?\n Presiona 1 de lo contrario presiona 2")
    bandera = int(input())

print("FIN")