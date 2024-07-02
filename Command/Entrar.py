from Command.Command import Command

class Entrar(Command):
    
    def ejecutar(self, obj):
        self.receiver.entrar(obj)
    
    def esEntrar(self):
        return True
    
    def __str__(self):
        return "¡ENTRANDO!"
    
    def equals(self,comando):
        if comando.esEntrar():
            return True
        return False