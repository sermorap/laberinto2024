from Estado.Estado import Estado

class Abierta(Estado):
    
    def abrir(self, puerta):
        print("¡Puerta abierta de par en par!.")

    def estaAbierta(self):
        return True
    
    def esAbierta(self):
        return True
    
    def __str__(self):
        return "Abierta"
    
    def __repr__(self):
        return "Abierta"