import os
import sys

from ElementoMapa.Container.Laberinto import Laberinto
from ElementoMapa.Puerta import Puerta
from ElementoMapa.Container.Habitacion import Habitacion
from ElementoMapa.Pared import Pared
from Orientaciones.Norte import Norte
from Orientaciones.Este import Este
from Orientaciones.Oeste import Oeste
from Orientaciones.Sur import Sur
from ElementoMapa.Leaf.Decorator.Bomba import Bomba
from Artefactos.Arco import Arco
from Artefactos.BolsilloMagico import BolsilloMagico

from Ente.Bicho import Bicho
from Modo.Agresivo import Agresivo
from Modo.Perezoso import Perezoso
from Modo.SuperSaiyan import SuperSaiyan
from Juego.Juego import Juego
from ElementoMapa.Container.Armario import Armario
from Forma.Cuadrado import Cuadrado
from ElementoMapa.Leaf.Tunel import Tunel
from Command.Abrir import Abrir
from Artefactos.Comida import Comida
from Artefactos.Pocima import Pocima
from Command.Equipar import Equipar

class LaberintoBuilder():
    
    def __init__(self):
        self.juego = None
        self.maze = None
        self.dict = None

    def obtenerJuego(self):
        return self.juego
    
    def makeJuego(self):
        juego = Juego()
        juego.prototype = self.laberinto
        juego.laberinto = juego.clonarLaberinto()
        self.juego = juego

        return juego
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarModoSupersaiyan(self):
        return SuperSaiyan()
    
    def fabricarBicho(self):
        return Bicho()
    
    def fabricarComida(self,num):
        comida = Comida()
        comida.ref = num

        cmd = self.fabricarCoger()
        cmd.receiver= comida

        comida.addCommand(cmd)
        return comida
    
    def fabricarPocima(self,num):
        pocima = Pocima()
        pocima.ref = num

        cmd = self.fabricarCoger()
        cmd.receiver= pocima

        pocima.addCommand(cmd)
        return pocima
    
    def fabricarForma(self):
        return Cuadrado()
    
    def fabricarArmario(self, id):
        return Armario(id)
    
    def fabricarTunel(self):
        return Tunel()
    
    def fabricarTunelEn(self, parent):

        tunel = self.fabricarTunel()
        parent.addChild(tunel)

    def fabricarArmarioEn(self, obj, num):
        armario = self.fabricarArmario(num)
        
        parent = self.fabricarPuerta()
        cmd = Abrir()
        cmd.receiver= parent

        parent.addCommand(cmd)

        parent.lado1=self
        parent.lado2=obj

        armario.form = self.fabricarForma()
        parent.lado1 = armario
        parent.lado2 = obj

        armario.addOr(self.fabricarNorte())
        armario.addOr(self.fabricarEste())
        armario.addOr(self.fabricarOeste())
        armario.addOr(self.fabricarSur())

        armario.putElementOn(self.fabricarNorte(),self.fabricarPared())
        armario.putElementOn(self.fabricarEste(),self.fabricarPared())
        armario.putElementOn(self.fabricarOeste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSur(), parent)

        obj.addChild(armario)
        return armario

    def fabricarBombaEn(self,padre,num):
        bomba = self.fabricarBomba()
        bomba.num = num
        padre.addChild(bomba)

    def fabricarVenenoEn(self,padre,num):
        veneno = self.fabricarVenenoEn()
        veneno.num = num
        padre.addChild(veneno)
    
    def fabricarArcoEn(self,padre,num):
        arma = self.fabricarArco()
        arma.ref = num
        padre.addChild(arma)
        cmd = Equipar()
        arma.addCommand(cmd)
        
        return arma
    
    def fabricarBichoAgresivo(self, posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoAgresivo()

        bicho.corazones = 100
        bicho.poder = 50

        return bicho
    
    def fabricarBichoPerezoso(self, posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoPerezoso()

        bicho.corazones = 50
        bicho.poder = 25

        return bicho
    
    def fabricarBichoSupersaiyan(self, posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoSupersaiyan()

        bicho.corazones = 120
        bicho.poder = 75

        return bicho

    def fabricarBichoAlternativo(self, modo, posicion):
        hab = self.juego.getHab(posicion)

        if modo == "agresivo":
            bicho = self.fabricarBichoAgresivo(hab)
        if modo == "perezoso":
            bicho = self.fabricarBichoPerezoso(hab)
        if modo == "supersaiyan":
            bicho = self.fabricarBichoSupersaiyan(hab)
        
        if bicho is not None:
            self.juego.agregarBicho(bicho)
    
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarAbrir(self):
        return Abrir()

    def fabricarEquipar(self):
        return Equipar()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref = num
        hab.form = forma

        hab.putElementOn(self.fabricarNorte(),self.fabricarPared())
        hab.putElementOn(self.fabricarEste(),self.fabricarPared())
        hab.putElementOn(self.fabricarOeste(),self.fabricarPared())
        hab.putElementOn(self.fabricarSur(),self.fabricarPared())

        hab.addOr(self.fabricarNorte())
        hab.addOr(self.fabricarEste())
        hab.addOr(self.fabricarOeste())
        hab.addOr(self.fabricarSur())

        self.laberinto.agregarHabitacion(hab)

        return hab

    def fabricarPuertaL(self, num1, ori1, num2, ori2):
        l1 =self.laberinto.getHab(num1)
        l2 =self.laberinto.getHab(num2)

        ori1x = getattr(self,'fabricar'+ ori1)()
        ori2x = getattr(self,'fabricar'+ ori2)()

        door = self.fabricarPuerta()

        door.lado1 = l1 
        door.lado2 = l2

        com = self.fabricarAbrir()
        com.receiver = door
        door.addCommand(com)

        l1.putElementOn(ori1x, door)
        l2.putElementOn(ori2x, door)

    def fabricarComidaEn(self, obj, ref):
        obj.addChild(self.fabricarComida(ref))

    def fabricarPocimaEn(self, obj, ref):
        obj.addChild(self.fabricarPocima(ref))

    def fabricarPared(self):
        return Pared()

    def fabricarNorte(self):
        return Norte.obtenerInstancia()
    
    def fabricarEste(self):
        return Este.obtenerInstancia()
    
    def fabricarOeste(self):
        return Oeste.obtenerInstancia()
    
    def fabricarSur(self):
        return Sur.obtenerInstancia()
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarVeneno(self):
        return Bomba()
    
    def fabricarArco(self):
        return Arco()