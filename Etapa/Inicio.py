from Etapa.Etapa import Etapa
from Etapa.Desarrollo import Jugando

class Inicio(Etapa):
    
    def addCharacter(self, ch, game):
        game.puedeAgregarPersonaje(ch)

    def lanzarBichos(self,juego):
        juego.puedeLanzarBichos()
        juego.fase = Jugando()

    def esInicio(self):
        return True
