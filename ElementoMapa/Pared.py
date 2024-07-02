from ElementoMapa.ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    
    def entrar(self,ente):
        print("¡CUIDADO! ¡Que te chocas!")

    def aceptar(self,visitor):
        print("Estas en una pared.")
        visitor.visitaPared(self)

    def EstimarDistancia(self):
        pass

    def esPared(self):
        return True
    
    def __str__(self):
        return "Pared"
    
    def __repr__(self):
        return "Pared"