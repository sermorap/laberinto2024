from Forma.Pentagono import Pentagono
from LaberintoBuilder.LaberintoBuilder import LaberintoBuilder
from ElementoMapa.Container.Habitacion import Habitacion
from Orientaciones import Noroeste, Noreste, Sureste, Suroeste, Sur
from Command.Abrir import Abrir

class PentagonoBuilder(LaberintoBuilder):
    
    def fabricarForma(self):
        return Pentagono()
    
    def fabricarNoroeste(self):
        return Noroeste.obtenerInstancia()
    
    def fabricarNoreste(self):
        return Noreste.obtenerInstancia()
    
    def fabricarSureste(self):
        return Sureste.obtenerInstancia()
    
    def fabricarSuroeste(self):
        return Suroeste.obtenerInstancia()
    
    def fabricarSur(self):
        return Sur.obtenerInstancia()
    
    def fabricarHabitacion(self, num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref = num
        hab.form = forma

        hab.setElementEn(self.fabricarNoroeste(), self.fabricarPared())
        hab.setElementEn(self.fabricarNoreste(), self.fabricarPared())
        hab.setElementEn(self.fabricarSureste(), self.fabricarPared())
        hab.setElementEn(self.fabricarSuroeste(), self.fabricarPared())
        hab.setElementEn(self.fabricarSur(), self.fabricarPared())

        hab.addOrientaciones(self.fabricarNoroeste())
        hab.addOrientaciones(self.fabricarNoreste())
        hab.addOrientaciones(self.fabricarSureste())
        hab.addOrientaciones(self.fabricarSuroeste())
        hab.addOrientaciones(self.fabricarSur())

        self.laberinto.agregarHabitacion(hab)

        return hab
    
    def fabricarArmarioEn(self, padre, num):
        armario = self.fabricarArmario(num)
        
        p1 = self.fabricarPuerta()
        cmd = Abrir()
        cmd.receiver = p1

        p1.addCommand(cmd)

        p1.lado1 = armario
        p1.lado2 = padre

        armario.form = self.fabricarForma()

        armario.addOrientaciones(self.fabricarNoroeste())
        armario.addOrientaciones(self.fabricarNoreste())
        armario.addOrientaciones(self.fabricarSuroeste())
        armario.addOrientaciones(self.fabricarSureste())
        armario.addOrientaciones(self.fabricarSur())

        armario.putElementOn(self.fabricarNoreste(),self.fabricarPared())
        armario.putElementOn(self.fabricarNoroeste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSureste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSuroeste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSur(),p1)

        padre.addChild(armario)
        return armario
