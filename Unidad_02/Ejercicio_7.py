mapa=[
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#Reorriendo la matriz con ciclos anidados
#Ciclo externo para manejar filas(i)
for i in range(filas):#<4
    #Ciclo interno para manejar columnas(j)
    for j in range(columnas):
        #Verificamos al encontrar el tesoro
        if mapa[i][j]=="x":
            print(f"Tesoro encontrado en la posición [{i}][{j}]")
        if mapa [i][j]=="b":
                    print(f"Tesoro encontrado en la posición [{i}][{j}]")