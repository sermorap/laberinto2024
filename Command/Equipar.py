from Command.Command import Command

class Equipar(Command):
    
    def ejecutar(self, obj):
        self.receiver.entrar(obj)

    def esEquipar(self):
        return True
    
    def __str__(self):
        return "Equipando" + str(self.receiver)
    
    def equals(self,command):
        if command.esEquipar():
            return True
        return False