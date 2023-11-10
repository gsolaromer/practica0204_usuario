# Definir un diccionario para almacenar la base de datos de alumnado
base_de_datos_alumnos = {}
# Función para agregar un nuevo alumno/a a la base de datos
def agregar_alumno():
    # Solicitar los datos del alumno/a al usuario
    nif = input("Ingrese el NIF del alumno/a: ")
    nombre = input("Ingrese el nombre del alumno/a: ")
    apellidos = input("Ingrese los apellidos del alumno/a: ")
    telefono = input("Ingrese el teléfono del alumno/a: ")
    correo = input("Ingrese el correo del alumno/a: ")
    aprobado = input("¿Ha aprobado el módulo? (True/False): ").lower() == "true"
    # Crear un diccionario con los datos del alumno/a
    datos_alumno = {"Nombre": nombre,"Apellidos": apellidos, "Teléfono": telefono, "Correo": correo, "Aprobado": aprobado}
    # Agregar el diccionario de datos al diccionario principal usando el NIF como clave
    base_de_datos_alumnos[nif] = datos_alumno
# Función para eliminar un alumno/a de la base de datos
def eliminar_alumno():
    # Solicitar el NIF del alumno/a que se desea eliminar
    nif = input("Ingrese el NIF del alumno/a que desea eliminar: ")
    # Verificar si el NIF está presente en la base de datos y eliminar al alumno/a
    if nif in base_de_datos_alumnos:
        del base_de_datos_alumnos[nif]
        print(f"Alumno/a con NIF {nif} eliminado/a.")
    else:
        print(f"No se encontró al alumno/a con NIF {nif} en la base de datos.")
# Función para mostrar los datos de un alumno/a
def mostrar_alumno():
    # Solicitar el NIF del alumno/a que se desea mostrar
    nif = input("Ingrese el NIF del alumno/a que desea mostrar: ")
    
    # Verificar si el NIF está presente en la base de datos y mostrar los datos del alumno/a
    if nif in base_de_datos_alumnos:
        print(f"Datos del alumno/a con NIF {nif}:\n{base_de_datos_alumnos[nif]}")
    else:
        print(f"No se encontró al alumno/a con NIF {nif} en la base de datos.")
# Función para listar todos los alumnos/as de la base de datos
def listar_todo():
    print("Listado de todo el alumnado:")
    for nif, datos_alumno in base_de_datos_alumnos.items():
        print(f"NIF: {nif}, Nombre: {datos_alumno['Nombre']}")
# Función para listar solo los alumnos/as aprobados
def listar_aprobados():
    print("Listado del alumnado aprobado:")
    for nif, datos_alumno in base_de_datos_alumnos.items():
        if datos_alumno["Aprobado"]:
            print(f"NIF: {nif}, Nombre: {datos_alumno['Nombre']}")
# Bucle principal del programa
while True:
    # Mostrar el menú de opciones al usuario
    print("\nMenú:")
    print("(1) Añadir alumno/a")
    print("(2) Eliminar alumno/a")
    print("(3) Mostrar alumno/a")
    print("(4) Listar todo el alumnado")
    print("(5) Listar alumnado aprobado")
    print("(6) Terminar")
    # Solicitar al usuario que seleccione una opción del menú
    opcion = input("Seleccione una opción (1-6): ")
    # Evaluar la opción seleccionada y ejecutar la acción correspondiente
    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        eliminar_alumno()
    elif opcion == "3":
        mostrar_alumno()
    elif opcion == "4":
        listar_todo()
    elif opcion == "5":
        listar_aprobados()
    elif opcion == "6":
        print("Programa terminado.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")