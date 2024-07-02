from ElementoMapa.Leaf.Decorator.Decorator import Decorator
from Command.Entrar import Entrar
from Command.RetirarVeneno import RetirarVeneno

class Veneno(Decorator):

    def __init__(self):
        super().__init__()
        self.activo = True
        self.damage = 10
        self.obsActivo = []
        c = Entrar()
        c.receiver = self
        self.commands.append(c)
        retirar = RetirarVeneno(self)
        self.commands.append(retirar)

    def esVeneno(self):
        return True

    def agregarObservadoresActivo(self, obs):
        self.obsActivo.append(obs)

    def aceptar(self, visitor):
        print("Visitar veneno")
        visitor.visitarVeneno(self)

    def entrar(self, e):
        if self.activo:
            print("¡CUIDADO! ¡Que te envenenas!")
            calculo = e.corazones - self.damage
            e.setCorazones(calculo)

            self.activo = False

            for co in self.commands:
                if co.esEntrar():
                    self.commands.remove(co)
            for obs in self.obsActivo:
                obs.visualVeneno(self)
        else:
            if self.componente is not None:
                self.componente.entrar(e)
    
    def retirarVeneno(self):
        if self.activo:
            self.activo = False
            print("El veneno ha sido retirado.")
            for obs in self.obsActivo:
                obs.visualVeneno(self)
        else:
            print("Ya no hay veneno.")