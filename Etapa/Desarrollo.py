from Etapa.Etapa import Etapa

class Desarrollo(Etapa):

    def addCharacter(self, ch, juego):
        print("[¡!] Juego en funcionamiento, no puedes añadir más personas [¡!]")

    def lanzarBichos(self, ch, juego):
        print("[¡!] Juego en funcionamiento, no puedes añadir más bichos [¡!]")
    
    def esJugando(self):
        return True
    