from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    
    def __init__(self):
        self.padre = None
        self.commands = []

    @abstractmethod 
    def entrar(self,ente):
        pass
    
    @abstractmethod
    def aceptar(self,visitor):
        pass

    def addCommand(self, command):
        for c in self.commands:
            if c.equals(command):
                return
        command.receiver = self
        self.commands.append(command)

    def obtenerComandos(self, ente):
        return self.commands
    
    def deleteCommand(self, command):
        self.commands.remove(command)

    def recorrer(self, fn):
        fn(self)

    def esHabitacion(self):
        return False
    
    def esBomba(self):
        return False
    
    def esVeneno(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False
    
    def esArco(self):
        return False

    def esArmario(self):
        return False
    
    def esTunel(self):
        return False
    
    def esBolsilloMagico(self):
        return False
    
    def esComida(self):
        return False
    
    def esPocima(self):
        return False