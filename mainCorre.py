import time
from introduccion import Introduccion
from fin import Fin
from creaPersona import romualdo
from eleccion import Eleccion
from opciones import *
from diccCaminos import diccionarioCaminos
from diccPistas import diccionarioPistas
from siVivo import sigueVivo
from pistaCam import pistaCamino

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CORRE ROMUALDO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Declaración de variables y estados iniciales
distanciaRecorrida = 0 # Empezamos en 0 por ahora je

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Parte principal del programa
while romualdo.Viviendo:

    caminoUno = primerCamino() # Asigno uno de los posibles caminos a la opcion 1 de forma aleatoria
    pistaUno = pistaCamino(caminoUno) # Asigno una pista para mostrar en funcion del camino generado para la opcion 1

    caminoDos = segundoCamino() # Asigno uno de los posibles caminos a la opcion 2 de forma aleatoria
    pistaDos = pistaCamino(caminoDos) # Asigno una pista para mostrar en funcion del camino generado para la opcion 2

    if distanciaRecorrida == 0:
        Introduccion() # Llamo a la introduccion
        Opciones(pistaUno, pistaDos) # Llamo la funcion para mostrar las opciones de camino
        unCamino = Eleccion() # Llamo a la funcion para que el usuario elija un camino
    else:
        Opciones(pistaUno, pistaDos) # Llamo la funcion para mostrar las opciones de camino
        unCamino = Eleccion() # Llamo la funcion para que el usuario elija un camino

    # En base a lo que elige el jugador, muestra un camino o el otro
    if unCamino == 1:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", diccionarioPistas[pistaUno],"\ny", diccionarioCaminos[caminoUno])
        sigueVivo(caminoUno)
        time.sleep(2)
        romualdo.Check() # Imprimo el estado del personaje
    elif unCamino == 2:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", diccionarioPistas[pistaDos],"\ny", diccionarioCaminos[caminoDos])
        sigueVivo(caminoDos)
        time.sleep(2)
        romualdo.Check() # Imprimo el estado del personaje

Fin(distanciaRecorrida) # Mostramos el mensaje de fin