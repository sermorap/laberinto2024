from Artefactos.Artefacto import Artefacto
from Command.Usar import Usar
from Command.Dejar import Dejar


class Arco(Artefacto):

    def __init__(self):
        super().__init__()
        self.poder = 25

    def esArco(self):
        return True

    def aceptar(self, vst):
        print("Visitar arco")
        vst.visitarArco(self)
    
    def usar(self, o):
        o.setArco(self)
        o.bolsillomagico.usado(self)

        for c in self.commands:
            if c.esDejar():
                self.deleteCommand(c)
        for c in self.commands:
            if c.esUsar():
                self.deleteCommand(c)
    
    def desequipar(self,ente):
        ente.setArco(None)
        ente.bolsillomagico.addArtefacto(self)
        
        firstAction = Usar()
        firstAction.receiver= self

        secondAction = Dejar()
        secondAction.receiver = self

        self.addCommand(firstAction)
        self.addCommand(secondAction)

    def __str__(self):
        return "Arco ID: " +str(self.ref)