import random
def dameDado():
    return random.randrange(1, 7)

def dameTirada(cantidadDados):
    lista_dados = []
    for i in range(0,cantidadDados):
        lista_dados.append(dameDado())
    return lista_dados


tirada=dameTirada(5)

def ordenar_tirada(tirada):
    tirada_ordenada=sorted(tirada)
    return tirada_ordenada

def esSimple(tirada):
    if (tirada!=esEscalera or tirada!=esFull or tirada!=esPoker ):
        return print('tu juego es: ',tirada)

def esEscalera(tirada_ordenada):
    if(tirada_ordenada==[1,2,3,4,5] or tirada_ordenada==[2,3,4,5,6]):
       return True

def esFull(tirada_ordenada):
   if(tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[3]==tirada_ordenada[4] or tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[2]==tirada_ordenada[3] and tirada_ordenada[3]==tirada_ordenada[4]):
       return True

def esPoker(tirada_ordenada):
    if(tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2]and tirada_ordenada[2]==tirada_ordenada[3] or tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[2]==tirada_ordenada[3]and tirada_ordenada[3]==tirada_ordenada[4]):
        return True

def esGenerala(tirada):
    if tirada[0] == tirada[1] == tirada[2] == tirada[3] == tirada[4]:
        return True

jugadas = [esGenerala,esPoker,esFull,esEscalera]
nombres = ["Generala", "Poker", "Full", "Escalera"]
mostrar_tirada=ordenar_tirada(tirada)
resultado=esSimple(mostrar_tirada)
#resultado1=esEscalera(mostrar_tirada)
#resulatao2=esFull(mostrar_tirada)
#resultado3=esPoker(mostrar_tirada)
#resultado4=esGenerala(mostrar_tirada)

for i in range(0,4):
    if jugadas[i](mostrar_tirada):
        print(nombres[i])
        break