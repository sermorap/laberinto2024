from ElementoMapa.Pared import Pared
from Command.RetirarVeneno import RetirarVeneno

class ParedVeneno(Pared):
    def __init__(self):
        super().__init__()
        self.commands.append(RetirarVeneno(self))

    def obtenerComandos(self, ente):
        return self.commands

    def aceptar(self, visitor):
        visitor.visitar(self)

    def __str__(self):
        return "Pared Envenenada"