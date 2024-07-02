from ElementoMapa.Container.Habitacion import Habitacion
from ElementoMapa.ParedVeneno import ParedVeneno

class HabitacionFuego(Habitacion):
    def __init__(self, ref):
        super().__init__(ref)
        self.pared = ParedVeneno()
        self.ref = ref

    def obtenerComandos(self, ente):
        return self.pared.obtenerComandos(ente)

    def aceptar(self, visitor):
        visitor.visitar(self)

    def __str__(self):
        return "Habitación Envenenada"