from Forma.Forma import Forma

class Rombo(Forma):

    def __init__(self):
        super().__init__()

        self.noreste = None
        self.noroeste = None
        self.suroeste = None
        self.sureste = None
        self.sur = None

    def esPentagono(self):
        return True

    def __str__(self):
        return "\n   -Noreste: " + str(self.noreste) +"\n   -Noroeste: " + str(self.noroeste) +"\n   -Sureste: " + str(self.sureste) +"\n   -Suroeste: " + str(self.suroeste) +"\n   -Sur: " + str(self.suro)
 