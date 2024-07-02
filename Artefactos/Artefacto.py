from Command.Usar import Usar
from Command.Equipar import Equipar
from Command.Dejar import Dejar

from ElementoMapa.ElementoMapa import ElementoMapa
from abc import ABC,abstractmethod

class Artefacto(ElementoMapa, ABC):
    
    def __init__(self):
        super().__init__()
        self.ref = None
        self.obsPos = []
        
    def entrar(self, obj):
        
        if self in self.padre.objChildren:
            self.padre.objChildren.remove(self)
        else:
            print(f"Error: {self} no está en la lista objChildren de {self.padre}")
        obj.bolsillomagico.addArtefacto(self)

        for com in self.commands:
            if com.esEquipar():
                self.deleteCommand(com)

        self.addCommand(Dejar())
        self.addCommand(Usar())
        for obs in self.obsPos:
            obs.visualObjeto(self)

    def dejar(self,ente):
        ente.posicion.addChild(self)
        ente.bolsillomagico.soltarArtefacto(self)
        for com in self.commands:
            if com.esDejar():
                self.deleteCommand(com)
        for com in self.commands:
            if com.esUsar():
                self.deleteCommand(com)
        self.addCommand(Equipar())
        for obs in self.obsPos:
            obs.visualObjeto(self)

    def agregarObservadorPosicion(self, observador):
        self.obsPos.append(observador)

    @abstractmethod
    def usar(self, obj):
        pass