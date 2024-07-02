from abc import ABC, abstractmethod

class Command(ABC):
    
    def __init__(self):
        self.receiver = None
        
    @abstractmethod
    def ejecutar(self, ente):
        pass

    def esAbrir(self):
        return False
    
    def esCerrar(self):
        return False
    
    def esEntrar(self):
        return False
    
    def esUsar(self):
        return False
    
    def esEquipar(self):
        return False
    
    def esDejar(self):
        return False
    
    def esRetirar(self):
        return False
    
    @abstractmethod
    def equals(self,command):
        pass
    