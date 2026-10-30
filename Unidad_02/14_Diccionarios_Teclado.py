#1. Creamos un diccionario
nuevo_usuario = {}
#2. pedimos los datos desde el teclado
nuevo_usuario["Nombre"] = input("Ingresa el nombre: ")
nuevo_usuario["Edad:"] = float(input("ingresa la edad: "))
nuevo_usuario["Estatura:"] = float(input("Ingresa tu estatura en metros: "))
print("\n ---Información Guardada----")
#Mostrando la información del diccionario
print(nuevo_usuario)