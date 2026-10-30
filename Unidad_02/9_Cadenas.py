#Cadenas y concatenación con (+)
Cadena1='Hola'
Cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(Cadena1 + Cadena2 + multilinea)
#Cadenas y repetición
eco = "ja"*5
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre ='Fany'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a minusculas
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase = "Me gusta programamción"
print(frase.replace("Programación","Historia"))
#Formato de cadenas (F-String)
edad = 18
Nombre = 'Fany'
mensaje = f"Hola, me llamo"
print (mensaje)
#Contar los caracteres de una cadena
text = "¡Felicidades por aun continuar en el CECY!"
cantidad_caracteres = len(texto)