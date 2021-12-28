import time

# Funcion para que el jugador elija un camino
def Eleccion():

    camino = ""
    letras = 0

    # Loop para que el jugador elija un camino, solo sale del loop si elige 1 o 2
    # El try-except es para evitar que el programa caiga si ingresa una letra
    while camino != 1 and camino != 2:
        try:
            camino = int(input("\n¿Camino 1 o camino 2?: "))
            time.sleep(2)
        except ValueError:
            print("\n¡ATENCION!\nNo se pueden ingresar letras.\nPor favor vuelve a intentarlo.")
            letras = letras + 1
            if letras >= 3:
                print("\nLos caracteres permitidos son el numero 1 y el numero 2.\nPor favor vuelve a intentarlo.")
    return camino