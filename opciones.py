import time
from diccPistas import diccionarioPistas
from camAleatorio import caminoAleatorio

def primerCamino():
    cam1 = caminoAleatorio()
    return cam1

def segundoCamino():
    cam2 = caminoAleatorio()
    return cam2

# Funcion que nos muestra las opciones de camino disponibles para elegir, con pistas
def Opciones(pista_1, pista_2):

    if diccionarioPistas[pista_1] == diccionarioPistas[pista_2]:
        print("El camino 1 parecen que",diccionarioPistas[pista_1],", y el camino 2... Tambien!") # Muestra si ambas pistas son iguales
        time.sleep(1)
        print("\nElige con cuidado, tu vida depende de ello...")
    else:
        print("1. Este camino parece que",diccionarioPistas[pista_1]) # Muestra una pista de lo que parece que hay en el camino 1
        print("2. Este camino parece que",diccionarioPistas[pista_2]) # Muestra una pista de lo que parece que hay en el camino 2
        time.sleep(1)
        print("\nElige con cuidado, tu vida depende de ello...")