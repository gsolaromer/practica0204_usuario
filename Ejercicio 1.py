divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

opcion = str(input("Que divisa deseas visualizar?\n"))
opcion = opcion.title()

if opcion in divisas:
    print(divisas[opcion])
else:
    print("No se encontro la divisa :(")