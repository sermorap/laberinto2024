from abc import ABC, abstractmethod

class Etapa(ABC):
    
    @abstractmethod
    def addCharacter(self, ch, game):
        pass
    
    @abstractmethod
    def lanzarBichos(self, game):
        pass

    def esInicio(self):
        return False
    
    def esDesarrollo(self):
        return False
    
    def esFinal(self):
        return False