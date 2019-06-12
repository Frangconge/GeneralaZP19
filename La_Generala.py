#se inicia con todos los import."

import random
#para una configuracion de azar que se usara en los dados ha jugar.

from tabulate import tabulate
#para crear la tabla donde se mostraran los puntos anotados por los jugadores

import sqlite3
#para la base de datos donde se guardaran los datos de jugadores y la puntiacion que vayan obteniendo

import os
#se continua con todos los "def" es decir las funciones que llevara acabo el proceso.
#se crea un def para un menu, en el se establece la obcion de partida nueva , reglas del juego y salir del juego
def Menu():

    os.system('cls')
    print("SELECCIONA UN OPCION: ")
    print("\t1 - Reglas de Juego ")
    print("\t2 - New Game / Juego nuevo")
    print("\t3 - Out / Salir ")
#mostramos el menu
while True:
    Menu()
    #solicitamos una opcion al usuario
    opcionMenu = input("Inserta el numero de la opcion >> ")

    if (opcionMenu=="1"):
        print("REGLAS DEL JUEGO:\n"
              "<< LA GENERALA >>\n"
              "\n"
              "La generala es un juego de dados.\n"
              "Se juega con cinco dados y un cubilete; el número de jugadores es ilimitado,\n"
              "pero lo ideal es de 3 a 5.\n"
              "El objetivo del juego es lograr la mayor puntuación,\n"
              "de acuerdo a la valoración establecida para cada jugada posible en el juego,\n"
              "llamada categoría.\n"
              "\n"
              "Se establece el orden de los jugadores\n"
              "\n"
              "Existen 11 posibles categorías, por lo que cada jugador tendrá 11 tiros posibles en el juego.\n"
              "Cada tirada consiste en el lanzamiento de los cinco dados\n"
              "y según sean los números que salgan se podrá optar a una categoría;\n"
              "si no se logra alcanzar una categoría satisfactoria en el primer lanzamiento se pueden apartar los dados útiles\n"
              "y tomar los demás y tirarlos de nuevo; en esta segunda tirada se pueden apartar otra vez los más convenientes \n"
              "y juntarlos con los que ya tenía apartados, y luego se tirará el resto por tercera y última vez,\n"
              "con lo que termina la tirada.\n"
              "\n"
              "los dados se enumeran del 1 al 5 respectivamente de izq a derch,\n"
              "es decir, si quieres volver a tirar uno o varios dados\n"
              "ingrese el numero del dado que vuelve al cubilete, sea el dado 1, 2, 3, 4 ó 5\n"
              'en caso de tirarlos todos de vuelta presiona "T"\n'
              'o si decides Plantarte con la jugada obtenida presiona "P"\n'
              "\n"
              "Si en el primer tiro se logró una categoría, a esto se lo llama «tiro servido» \n"
              "La puntuación se establece en relación a la categoría que se obtiene con la combinación de los 5 dados.\n"
              "Cuando se optine una tirada servida, a la puntuacion se le añaden 5pts adicionales. "
              "\n"
              "Se anotara la puntuación de cada jugador en una planilla donde estan las once categorías posibles,\n"
              'que van de la categoría 1 a la 6 y luego las categorías que se llaman "Juegos mayores", \n'"
              "que son escalera, full, póquer, generala y doble generala.\n"
              "\n"
              "CATEGORIAS\n"
              "- Del 1 al 6: Para calcular el puntaje correspondiente a la categoría se suman los números iguales.\n"
              "- Escalera:  "
                                                                                                                                                                                                                            " En los encabezados, formando columnas verticales, se colocan los nombres de los jugadores")





    elif (opcionMenu=="2"):
        print("JUEGO NUEVO")
        NewGame = input("Desea iniciar un juevo nuevo? S / N >> ").upper()
        if (NewGame=="N"):
            print("Hasta la Proxima.")
            break

    elif (opcionMenu=="3"):
        print("Hasta la Proxima.")
        break


