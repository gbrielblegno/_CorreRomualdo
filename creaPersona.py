import time

# Creo la clase persona para poder darle atributos al jugador.
class Persona():
    def __init__(self, nombre, vida, viviendo, cansancio, hambre):
        self.Nombre = nombre
        self.Vida = vida
        self.Viviendo = viviendo
        self.Cansancio = cansancio
        self.Hambre = hambre

    def Estado(self):
        print("Nombre:", self.Nombre,"\nVida:", self.Vida,"%\nSigue vivo:", self.Viviendo,"\nCansancio:",self.Cansancio,"%","\nHambre:",self.Hambre,"%")

    def Check(self):

        if self.Cansancio >= 75 or self.Hambre >= 75:
            self.Vida = self.Vida - 10

        if self.Cansancio < 0:
            self.Cansancio = 0
        elif self.Cansancio > 100:
            self.Cansancio = 100

        if self.Hambre > 100:
            self.Hambre = 100
        elif self.Hambre < 0:
            self.Hambre = 0

        if self.Viviendo == False:
            self.Vida = 0
        elif self.Vida == 0:
            self.Viviendo = False
            print("Tu vida llego a 0...\n")
        elif self.Vida > 100:
            self.Vida = 100

        if self.Viviendo == True:
            if self.Cansancio >= 75 and self.Vida <= 25 and self.Hambre >= 75:
                print("Estas muy cansado, herido y hambriento...")
            elif self.Cansancio >= 75 and self.Vida > 25 and self.Hambre < 75:
                print("Estas muy cansado...")
            elif self.Cansancio < 75 and self.Vida <= 25 and self.Hambre < 75:
                print("Estas muy herido...")
            elif self.Cansancio < 75 and self.Vida > 25 and self.Hambre >= 75:
                print("Estas muy hambriento...")
            elif self.Cansancio >= 75 and self.Vida <= 25 and self.Hambre < 75:
                print("Estas muy cansado y herido...")
            elif self.Cansancio >= 75 and self.Vida > 25 and self.Hambre >= 75:
                print("Estas muy cansado y hambiriento...")
            elif self.Cansancio < 75 and self.Vida <= 25 and self.Hambre >= 75:
                print("Estas muy herido y hambriento...")

            if self.Cansancio >= 75 or self.Vida <= 25 or self.Hambre >= 75:
                time.sleep(1)
                print("Tienes que encontrar un poblado pronto o moriras...")

            print("Te quedan",self.Vida,"% ","de vida.\nTu nivel de cansancio es",(self.Cansancio),"%","\nTu nivel de hambre es",self.Hambre,"%\n")

romualdo = Persona("Romualdo",100,True,0,25) # Defino de momento nombre, vida y estado de manera estatica al principio