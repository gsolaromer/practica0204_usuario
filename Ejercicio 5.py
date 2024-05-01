diccionario = {}

palabras = input("Escribe las palabras en el formato: - hola: hello, perro:dog,casa:house -")

for i in palabras.split(","):
    clave, valor = i.split(":")

    diccionario[clave] = valor

frase = input("Escribe una frase en español para traducir:\n")

for j in frase.split(" "):
    if j in diccionario:
        print(diccionario[j], end=" ")
    else:
        print(j, end=" ")