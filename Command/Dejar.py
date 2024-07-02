from Command.Command import Command

class Dejar(Command):
    
    def ejecutar(self, obj):
        self.receiver.dejar(obj)

    def esDejar(self):
        return True
    
    def __str__(self):
        return "Dejando" + str(self.receiver)
    
    def equals(self,command):
        if command.esDejar():
            return True
        return False