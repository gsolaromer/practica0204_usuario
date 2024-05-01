alumnos = {}
bandera = "s"

while bandera == "s":
    op =input("MENU\nQue opcion deseas realizar\n(1)Agregar alumno\n(2)Eliminar alumno\n(3)Mostrar alumno\n(4)Listar todo el alumnado\n(5)Listar alumnado aprobado\n(6)SALIR\n")

    if op == "1":
        nif = input("NIF: ")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        aprobado = input("Es alumno aprobado?(true/false): ")
        aprobado = aprobado.lower()
        alumno = {"nombre":nombre,"apellidos":apellidos,"telefono":telefono,"correo":correo,"aprobado":aprobado}
        alumno[nif]=alumno

    elif op == "2":
        nif = input("ELIMINAR ALUMNO\nEscribe el NIF del alumno:\n")
        if nif in alumnos:
            for clave, valor in alumnos[nif].items():
                print(clave + " : " + valor)
                
            del(alumnos[nif])
            print("ALUMNO ELIMINADO\n")

        else:
            print("Este alumno no existe\n")
        print("\n")

    elif op == "3":
        nif = input("\nBUSCAR ALUMNO\nEscribe el NIF del alumno:\n")
        if nif in alumnos:
            for clave, valor in alumnos[nif].items():
                print(clave + " : " + valor)

        else:
            print("Este alumno no existe\n")
        print("\n")

    elif op == "4":
        for nif in alumnos:
            print("-------------------------------")
            for clave, valor in alumnos[nif].items():
                print(clave + " : " + valor)

    elif op == "5":
        for j in alumnos:
            for k in alumnos[j].items():
                if "true" in k:
                    for y in alumnos[j].items():
                        if "nombre" in k:
                            clave = k[0].title()
                            valor = k[1].title()
                    print("Alumno aprobado: "+ j +" "+clave+":"+valor+"\n")
                    
    elif op == "6":
        bandera = "n"