promedio=[9,19,6,5,7]
#1. Encontrar el promedio más bajo usando un ciclo for
#Suponemos inicialmente que el promedio mas bajo es
promedio_bajo = promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
print(promedio_bajo)