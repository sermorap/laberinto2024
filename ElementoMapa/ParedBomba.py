from ElementoMapa.Pared import Pared

class ParedBomba(Pared):

    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self,ente):
        if self.activa:
            print("¡¡¡¡La bomba te explotó en la cara!!!!")
            self.activa = False
        else:
            print("¡CUIDADO! ¡Que te chocas!")