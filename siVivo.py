from creaPersona import *

# Funcion que devuelve si romualdo continua con vida o no
def sigueVivo(vive):

    # Se cansa 10 por camino normal y mejora 10 si descansa
    # El hambre aumenta 10 por camino normal y mejora 10 si come un poco
    # El pueblo elimina todo el cansancio y el hambre, y restaura toda la vida

    if vive == "Camino_1":
        romualdo.Viviendo = False
        romualdo.Vida = 0 # Muere, los demas parametros no importan tanto
        #romualdo.Cansancio = 0
        #romualdo.Hambre = 0
        return False
    elif vive == "Camino_2":
        romualdo.Viviendo = True
        romualdo.Vida = romualdo.Vida + 10
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return True
    elif vive == "Camino_3":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 40 # Se cansa 2 por cada metro escalado + 10 por el camino
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_4":
        romualdo.Viviendo = True
        romualdo.Vida = romualdo.Vida - 20
        romualdo.Cansancio = romualdo.Cansancio + 20
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_5":
        romualdo.Viviendo = True
        romualdo.Vida = romualdo.Vida - 20
        romualdo.Cansancio = romualdo.Cansancio + 20
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_6":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_7":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return True
    elif vive == "Camino_8":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return True
    elif vive == "Camino_9":
        romualdo.Viviendo = True
        romualdo.Vida = 100
        romualdo.Cansancio = 0
        romualdo.Hambre = 0
        return False
    elif vive == "Camino_10":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_11":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 30
        romualdo.Hambre = romualdo.Hambre + 50
        return True
    elif vive == "Camino_12":
        romualdo.Viviendo = False
        romualdo.Vida = 0 # Muere, los demas parametros no importan tanto
        #romualdo.Cansancio = 0
        #romualdo.Hambre = 0
        return True
    elif vive == "Camino_13":
        romualdo.Viviendo = False
        romualdo.Vida = 0 # Muere, los demas parametros no importan tanto
        #romualdo.Cansancio = 0
        #romualdo.Hambre = 0
        return True
    elif vive == "Camino_14":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_15":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_16":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_17":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return False
    elif vive == "Camino_18":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_19":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    else:
        return "Verificar porque algo anda mal... sigueVivo()"