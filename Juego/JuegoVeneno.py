from Juego.Juego import Juego
from ElementoMapa.Container.HabitacionVeneno import HabitacionVeneno
from ElementoMapa.ParedVeneno import ParedVeneno

class JuegoVeneno(Juego):

    def fabricarHabitacion(self, id):
        return HabitacionVeneno(id)

    def fabricarPared(self):
        return ParedVeneno()
    
juego = JuegoVeneno()
juego.laberinto2HabFM()

hab = juego.laberinto.getHab(1)
print(juego.laberinto)
print(hab.entrar())
print(hab.entrar())
print(hab.norte.entrar())
print(hab.norte.entrar())