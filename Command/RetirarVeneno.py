from Command.Command import Command

class RetirarVeneno(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def ejecutar(self, obj):
        print(f"Retirando veneno de {self.receiver}")

    def esRetirar(self):
        return True

    def __str__(self):
        return "VENENO RETIRADO"

    def equals(self, command):
        if command.esRetirar():
            return True
        return False