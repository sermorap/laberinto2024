from Artefactos.Artefacto import Artefacto

class Pocima(Artefacto):
#
    def __init__(self):
        super().__init__()
        self.vida = 50

    def esPocima(self):
        return True
    
    def aceptar(self, vst):
        print("Pócima Astérix y Obélix encontrada")
        vst.visitarPocion(self)

    def usar(self, o):
        o.setCorazones(o.corazones + self.vida)
        o.bolsillomagico.usado(self)

    def __str__(self):
        return "Pócima ID: " + str(self.ref)