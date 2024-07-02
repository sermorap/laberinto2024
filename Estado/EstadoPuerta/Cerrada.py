from Estado.Estado import Estado

class Cerrada(Estado):
    
    def abrir(self,puerta):
        puerta.puedeAbrirse()
        print("¡Puerta cerrada para que no se escape el gato!.")

    def estaAbierta(self):
        return False
    
    def esCerrada(self):
        return True
    
    def __str__(self):
        return "Cerrada"
    
    def __repr__(self):
        return "Cerrada"