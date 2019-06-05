#import sqlite3

from tabulate import tabulate
#import turtle
window = Tk()
menu = Menu(window)
window.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "juego nuevo", menu = filemenu)
#se crea la funcion de culsuntar o no por las instrucciones del juego.

def consulta_instrucciones():
    I_consulta = input('deseas consultar las instrucciones acerca del juego de "La Generala" => S / N : ').upper()
    if (I_consulta == "S"):

#def procesa_turno_jugador(jugador_nombre):
#El código ejecuta el turno para cada jugador.
#Si devuelve False, continuamos con el juego.
#Si devuelve True, alguien ha ganado así que paramos. """
    #psi, angulo = entrada_usuario = obtener_datosdel_usuario(jugador_nombre)

    #distancia_boladebarro = calcular_distancia(psi, angulo)
    #diferencia = distancia_boladebarro - distancia_aparte

# Si echamos un vistazo al capítulo de formatos de impresión, estas líneas
# podrían imprimir números en un bonito formato.

    #if diferencia > 1:
        #print("Ha caído", diferencia, "metros muy lejos!")
    #elif diferencia < -1:
        #print("Te has quedado", diferencia * -1, "metros corto!")
    #else:
        #print("Bingo!", jugador_nombre, "gana!")
        #return True

    #print()
    #return False

#se hace el registro de cant y nombre de jugadores y los mismos se muestran en una tabla.



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