info = {"nombre":"","edad":"","direccion":"","telefono":""}

for i in info:
    dato = str(input("Cual es tu "+ i + "\n"))
    info[i]=dato

print(info["nombre"] + " tiene " + info["edad"] + " años,vive en " + info["direccion"] + " y su número de teléfono es " + info["telefono"])