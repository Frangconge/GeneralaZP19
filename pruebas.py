import random

# import registro_usuarios

def anotacionPuntos():
    return registro_usuarios

def dameTirada(cantidadDados):
    lista_dados = []
    for i in range(0,cantidadDados):
        lista_dados.append(random.randrange(1, 7))
    return lista_dados

def ordenar_tirada(tirada):
    tirada_ordenada=sorted(tirada)
    return tirada_ordenada

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


def infocambiaDado():
    print('los dados se enumeran del 1 al 5 respectivamente de izq a derch,'
                 ' es decir, se quieres volver a tirar uno o varios dados '
                 'ingrese el numero del dado que vuelve al cubilete, sea el dado 1, 2, 3, 4 ó 5'
                 'en caso de tirarlos todos de vuelta presiona "T" '
                 'de que Paltarte con la jugada obtenida presiona "P" ')

def cambiaDados(cubil):
    print(cubil)
    cambiaDados= input('desea volver al tirar algun dado? : S o N').upper()
    if (cambiaDados=="S"):
        intentos = 1
        while intentos < 3:
            print(cubil)
            d = input("Ingrese posición del dado a cambiar (separado por un punto): ")
            f = d.split(".")
            for t in f:
                cubil(int(t) - 1)
            print(cubil)
            intentos += 1
    elif (cambiaDados =="N"):
        input('si quieres tirar todo de vuelta presiona "T"'
              'si quieres plantarte con la jugada obtenida presione "P"').upper()
        if (cambiaDados=="T"):
             print (dameTirada(5))
        else:
           if (cambiaDados=="P"):
               return  cubil

def ValorarJugada():
    return


def cubilete():
    Cubilete=(input('presione "C" para ejecutar la tirada del cubilete: ')).upper()
    if (Cubilete=="C"):
        tirada = dameTirada(5)
    return tirada


    #jugadas = {'Generala': esGenerala(tirada),'Poker' :esPoker(tirada), 'Full' :esFull(tirada),'Escalera': esEscalera(tirada),'Simple':esSimple(tirada)}
    #resultado1=esEscalera(mostrar_tirada)
    #resulatao2=esFull(mostrar_tirada)
    #resultado3=esPoker(mostrar_tirada)
    #resultado4=esGenerala(mostrar_tirada)

    print(tirada)
    #print(sorted(jugadas.items(), key=operator.itemgetter(0)))
    #mostrarNombreDeJugada(jugadas)
cubil = cubilete()
print(cambiaDados(cubil))