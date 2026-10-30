#Creando una matriz
matriz=[
    [5,8,1],#Fila 01 1 x 3 columnas
    [3,9,2]#Fila 02 2 x 3 columnas
]
#Obteniendo el númer total de filas y columnas
filas=len(matriz)
columnas=len(matriz [0])
#Ciclo externo total de filas y coumnas
for i in range(filas):
    #Iclo interno para los indices de las columnas(j)
    for j in range(columnas):
        print(f"Posición[{i}][{j}]={matriz[i][j]}")