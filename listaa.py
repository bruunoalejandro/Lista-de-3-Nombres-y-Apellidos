nombres = []
apellidos = []
for i in range(3):
    nombre = input("Ingrese nombre: ")
    nombres.append(nombre)
    apellido = input("Ingrese apellido: ")
    apellidos.append(apellido)
for i in range(3):
    print(i+1, nombres[i], apellidos[i])