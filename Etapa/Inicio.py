from Etapa.Etapa import Etapa
from Etapa.Desarrollo import Desarrollo

class Inicio(Etapa):
    
    def addCharacter(self, ch, game):
        game.puedeAgregarPersonaje(ch)

    def lanzarBichos(self,juego):
        juego.puedeLanzarBichos()
        juego.fase = Desarrollo()

    def esInicio(self):
        return True
