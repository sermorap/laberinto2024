from Etapa.Etapa import Etapa

class Final(Etapa):
    
    def addCharacter(self, ch, juego):
        print("[¡!] El juego ha finalizado. No puedes añadir más personas [¡!]")

    def lanzarBichos(self,juego):
        print("[¡!] El juego ha finalizado. No puedes añadir más bichos [¡!]")
          
    def esFinal(self):
        return True
    