from LaberintoBuilder.LaberintoBuilder import LaberintoBuilder
from LaberintoBuilder.LaberintoRomboBuilder import LaberintoRomboBuilder
from LaberintoBuilder.LaberintoTrianguloBuilder import LaberintoTrianguloBuilder
from LaberintoBuilder.LaberintoRomboBuilder import LaberintoPentagonoBuilder
import json

class Director():
    
    def __init__(self):
        self.builder = None
        self.diccionario = None
        self.form = None

    def procesar(self, input):

        self.readConfig(input)
        self.iniBuilder()
        self.makeMaze()
        self.makeJuego()
        self.createAntagonist()

    def getJuego(self):
        return self.builder.obtenerJuego()


    def readConfig(self,unArchivo):

        with open(unArchivo, 'r', encoding='utf8') as file:
            self.diccionario = json.load(file)

    def iniBuilder(self):
        if self.diccionario['forma'] == "cuadrado":
            self.form = "Cuadrado"
            self.builder = LaberintoBuilder()
        if self.diccionario['forma'] == "rombo":
            self.form = "Rombo"
            self.builder = LaberintoRomboBuilder()
        if self.diccionario['forma'] == "triangulo":
            self.form = "Triangulo"
            self.builder = LaberintoTrianguloBuilder()
        if self.diccionario['forma'] == "pentagono":
            self.form = "Pentagono"
            self.builder = LaberintoPentagonoBuilder()

    def makeMaze(self):
        self.builder.fabricarLaberinto()

        for lab in self.diccionario['laberinto']:
            self.labRecursivo(lab,'root')

        for puerta in self.diccionario['puertas']:
            self.builder.fabricarPuertaL(puerta[0], puerta[1], puerta[2], puerta[3])

    def labRecursivo(self, dic, parent):
        if dic['tipo'] == 'habitacion':
            padre = self.builder.fabricarHabitacion(dic['num'])
        if dic['tipo'] == 'armario':
            padre = self.builder.fabricarArmarioEn(parent, dic['num'])
        
        if dic['tipo'] == 'bomba':
            padre = self.builder.fabricarBombaEn(parent, dic['num'])
        if dic['tipo'] == 'veneno':
            padre = self.builder.fabricarVenenoEn(parent, dic['num'])
        if dic['tipo'] == 'tunel':
            padre = self.builder.fabricarTunelEn(parent)

        if dic['tipo'] == 'comida':
            padre = self.builder.fabricarComidaEn(parent, dic['num'])
        if dic['tipo'] == 'pocima':
            padre = self.builder.fabricarPocimaEn(parent, dic['num'])
        if dic['tipo'] == 'arco':
            padre = self.builder.fabricarArcoEn(parent, dic['num'])

        hijos = dic.get('hijos',[])

        for h in hijos:
            self.labRecursivo(h, padre)


    def makeJuego(self):
        self.builder.makeJuego()

    def createAntagonist(self):
        antagonistas = self.diccionario.get('bichos',[])

        for ant in antagonistas:
            self.builder.fabricarBichoAlternativo(ant['modo'], ant['posicion'])