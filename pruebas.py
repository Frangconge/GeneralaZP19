import random
import operator
def dameDado():
    return random.randrange(1, 7)

def dameTirada(cantidadDados):
    lista_dados = []
    for i in range(0,cantidadDados):
        lista_dados.append(dameDado())
    return lista_dados

def ordenar_tirada(tirada):
    tirada_ordenada=sorted(tirada)
    return ordenar_tirada(tirada_ordenada)

def esSimple(tirada):

      return esEscalera(tirada)==False and esFull(tirada)==False and esPoker(tirada)==False and esGenerala(tirada)==False

def esEscalera(tirada_ordenada):
    if(tirada_ordenada==[1,2,3,4,5] or tirada_ordenada==[2,3,4,5,6]):
       return True
    else:
        return False
def esFull(tirada_ordenada):
   if((tirada_ordenada[0]==tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[2]!=tirada_ordenada[3]==tirada_ordenada[4] or
       tirada_ordenada[0]==tirada_ordenada[1]!=tirada_ordenada[2] and tirada_ordenada[2]==tirada_ordenada[3]==tirada_ordenada[4])):
       return True
   else:
       return False

def esPoker(tirada_ordenada):
    if(tirada_ordenada[0]==tirada_ordenada[1]==tirada_ordenada[2]==tirada_ordenada[3]!=tirada_ordenada[4] or
       tirada_ordenada[0]!=tirada_ordenada[1]==tirada_ordenada[2]==tirada_ordenada[3]==tirada_ordenada[4]):
        return True
    else:
        return False

def esGenerala(tirada):
    if (tirada[0] == tirada[1]) and(tirada[1] == tirada[2]) and (tirada[2] == tirada[3]) and (tirada[3] == tirada[4]):
        return True
    else:
        return False

def mostrarNombreDeJugada(jugadas):

    for clave in jugadas:
        if (jugadas[clave]==True):
            print(clave)


cubilete=(input('presione "C" para ejecutar la tirada del cubilete: ')).upper()
if (cubilete=="C"):
    tirada = dameTirada(5)

    jugadas = {'Generala': esGenerala(tirada),'Poker' :esPoker(tirada), 'Full' :esFull(tirada),'Escalera': esEscalera(tirada),'Simple':esSimple(tirada)}
     #resultado1=esEscalera(mostrar_tirada)
    #resulatao2=esFull(mostrar_tirada)
    #resultado3=esPoker(mostrar_tirada)
    #resultado4=esGenerala(mostrar_tirada)

    print(tirada)
    #print(sorted(jugadas.items(), key=operator.itemgetter(0)))
    mostrarNombreDeJugada(jugadas)

