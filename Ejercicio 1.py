diccionario = {'Euro':'€','Dollar':'$','Yen':'¥'}
divisa = input('Introduce una divisa ')
if divisa == "euro":
     print (f"Tu divisa es {diccionario['Euro']}")
elif divisa == "dollar":
     print (f"Tu divisa es {diccionario['Dollar']}")
elif divisa == "yen":
     print (f"Tu divisa es {diccionario['Yen']}")
else:
    print("Inserte una divisa, la de leer se la sabe?")