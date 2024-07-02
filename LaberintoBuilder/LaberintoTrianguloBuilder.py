from Forma.Triangulo import Triangulo
from LaberintoBuilder.LaberintoBuilder import LaberintoBuilder
from ElementoMapa.Container.Habitacion import Habitacion
from Orientaciones import Norte, Este, Suroeste
from Command.Abrir import Abrir

class LaberintoTrianguloBuilder(LaberintoBuilder):
    
    def fabricarForma(self):
        return Triangulo()
    
    def fabricarNorte(self):
        return Norte.obtenerInstancia()
    
    def fabricarEste(self):
        return Este.obtenerInstancia()
    
    def fabricarSuroeste(self):
        return Suroeste.obtenerInstancia()
    
    def fabricarHabitacion(self, num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref = num
        hab.form = forma

        hab.setElementEn(self.fabricarNorte(), self.fabricarPared())
        hab.setElementEn(self.fabricarEste(), self.fabricarPared())
        hab.setElementEn(self.fabricarSuroeste(), self.fabricarPared())

        hab.addOrientaciones(self.fabricarNorte())
        hab.addOrientaciones(self.fabricarEste())
        hab.addOrientaciones(self.fabricarSuroeste())

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

        armario.addOrientaciones(self.fabricarNorte())
        armario.addOrientaciones(self.fabricarEste())
        armario.addOrientaciones(self.fabricarOeste())

        armario.setElementEn(self.fabricarNorte(), self.fabricarPared())
        armario.setElementEn(self.fabricarEste(), self.fabricarPared())
        armario.putElementOn(self.fabricarOeste(), p1)

        padre.addChild(armario)
        return armario
    
