import random
dados = [0, 0, 0, 0, 0]

def tiro(*args):
    if not args:
        args = [0, 1, 2, 3, 4]
    for i in args:
        dados[i] = random.randrange(1, 7)
    return dados

def dameTirada():
    lista_dados = []
    for i in range(0,1):
        lista_dados.append(tiro())
    return lista_dados

def cambiaDados(*args):
    cubil = dameTirada()
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
             print (dameTirada())
        else:
           if (cambiaDados=="P"):
               return  cubil

cambiaDados()