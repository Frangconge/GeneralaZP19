from tabulate import tabulate

nombres = []
puntos = []
puntajes= ["Al 1","Al 2","Al 3","Al 4","Al 5", "Al 6","E","F","P","G","DG" ]
tablero = [0,0,0,0,0,0,0,0,0,0,0]
cant = int(input("ingrese cantidad de jugadores: "))

for i in range(0,cant):
    nombres.append(input("ingrese nombre del jugador: "))
    puntos.append(tablero)

listado = list(map(list,zip(*puntos)))

print (tabulate(listado,showindex=puntajes,headers=nombres, tablefmt="presto"))