# Crear un diccionario de traducción español-inglés
diccionario_traducción = {}
# Pedir al usuario que ingrese palabras y traducciones
print("Introduce las palabras y sus traducciones en formato palabra:traducción.")
print("Cuando quieras terminar, escribe 'terminar'.")
while True:
    entrada_usuario = input("Ingresa palabra y traducción (o escribe 'terminar' para finalizar): ").lower()
    if entrada_usuario == "terminar":
        break
    # Dividir la entrada en palabra y traducción
    partes = entrada_usuario.split(":")
    if len(partes) == 2:
        palabra, traducción = partes
        diccionario_traducción[palabra.strip()] = traducción.strip()
    else:
        print("Formato incorrecto. Debe ser palabra:traducción")
# Pedir al usuario que ingrese una frase en español
frase_español = input("Ingresa una frase en español: ")
# Traducir la frase palabra por palabra utilizando el diccionario
palabras_frase = frase_español.split()
frase_traducida = [diccionario_traducción.get(palabra, palabra) for palabra in palabras_frase]
# Mostrar la frase traducida
print("Frase traducida:")
print(" ".join(frase_traducida))