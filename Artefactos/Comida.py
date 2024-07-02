from Artefactos.Artefacto import Artefacto

class Comida(Artefacto):

    def __init__(self):
        super().__init__()
        self.vida = 10

    def esComida(self):
        return True
    
    def aceptar(self, vst):
        print("Comidita ricaaaaaa!!!!!!")
        vst.visitarBistec(self)

    def usar(self, o):
        o.setCorazones(o.corazones + self.vida)
        o.bolsillomagico.usado(self)

    def __str__(self):
        return "Comida nº: " + str(self.ref)
