from Ente.Ente import Ente
from Cuerpo.Cuerpo import Cuerpo
from Artefactos.BolsilloMagico import BolsilloMagico

class Personaje(Ente):
    
    def __init__(self):
        super().__init__()
        self.apodo=None
        self.bolsillomagico=None
        self.cuerpo=Cuerpo()

    def obtenerComandosCuerpo(self):
        return self.cuerpo.obtenerComandos()
    
    def obtenerArco(self):
        return self.cuerpo.obtenerArma()

    def setArco(self,obj):
        self.cuerpo.setArco(obj)

    def setPosicion(self, pos):
        self.posicion= pos
        for obs in self.obsPosition:
            obs.visualCuerpo()
    
    def setVidas(self, vida):
        self.vidas = vida
        print("",str(self) + "tiene : " + str(self.vidas) + " vidas")
        for obs in self.obsCoratzones:
            obs.visualcorazoneshero()
    
    def muere(self):
        self.juego.personajeMuere()

    def buscarEnemigo(self):
        return self.juego.searchAntagonist()
    
    def obtenerComandos(self,ente):
        return self.posicion.obtenerComandos(self)
    
    def esPersonaje(self):
        return True
    
    def __str__(self):
        return "Soy " + str(self.apodo)
    
    def __repr__(self):
        return "Soy " + str(self.apodo)