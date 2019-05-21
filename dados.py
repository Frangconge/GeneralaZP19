import random
def dameDado():
    return random.randrange(1, 7)

def dameTirada(cantidadDados):
    lista_dados = []
    for i in range(0,cantidadDados):
        lista_dados.append(dameDado())
    return lista_dados


print(dameTirada(5))