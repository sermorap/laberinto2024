from ElementoMapa.Container.Laberinto import Laberinto
from ElementoMapa.Puerta import Puerta
from ElementoMapa.Container.Habitacion import Habitacion
from ElementoMapa.Pared import Pared
from Orientaciones.Norte import Norte
from Orientaciones.Este import Este
from Orientaciones.Oeste import Oeste
from Orientaciones.Sur import Sur
from ElementoMapa.Leaf.Decorator.Bomba import Bomba
from ElementoMapa.Leaf.Decorator.Veneno import Veneno
from Artefactos.Arco import Arco
from Artefactos.BolsilloMagico import BolsilloMagico
from Ente.Bicho import Bicho
from Modo.Agresivo import Agresivo
from Modo.Perezoso import Perezoso
from Modo.SuperSaiyan import SuperSaiyan
from Etapa.Inicio import Inicio
from Etapa.Final import Final
import threading
import copy

class Juego():

    def __init__(self):

        self.maze = None
        self.prota = None
        self.bichos = []
        self.prototype = None
        self.threads={}
        self.lock = threading.Lock()
        self.etapa = Inicio()
        self.hasGanado = True

    def getHab(self, id):
        return self.laberinto.getHab(id)
        
    def getChildrenPosition(self):
        return self.prota.posicion.getChildren()
    
    def agregarPersonaje(self, ch):
        self.fase.addCharacter(ch, self)

    def puedeAgregarPersonaje(self, ch):
        ch.juego = self
        self.laberinto.entrar(ch)
        ch.bolsillo = BolsilloMagico()
        self.prota = ch

    def clonarLaberinto(self):
        return copy.deepcopy(self.prototype)
    
    def searchAntagonist(self, ente = None):

        if ente is None:

            pos = self.prota.posicion
        
            for ant in self.bichos:

                if ant.posicion == pos and ant.estaVivo():
                    return ant
        else:
            pos = ente.posicion

            for ant in self.bichos:
                if ant.posicion == pos and ant.estaVivo() and ant is not ente and ant.modo.esPerezoso():
                    return ant
        return None
    
    def searchCharacter(self, unBicho):
        if unBicho.posicion == self.prota.posicion:
            return self.prota
        else:
            return None
        
    def muereBicho(self):
        if self.verificarBichos() and self.hasGanado:
            print(str(self.prota),"HAS GANADO!")
            self.fase = Final()

    def verificarBichos(self):
        for ant in self.bichos:
            if ant.estaVivo():
                return False
        return True
    
    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarHilo(bicho)
    
    def terminarHilo(self, unBicho):
        unBicho.fenece()

    def personajeMuere(self):
        print(str(self.prota.seudonimo), " murió. ¡PERDISTE!")
        self.hasGanado = False
        self.terminarBichos()

        self.etapa = Final()
        
    def openDoors(self):
        def op(x):
            return x.abrir() if x.esPuerta() else None
        self.laberinto.recorrer(op)

    def cerrarPuertas(self):
        def op(x):
            return x.cerrar() if x.esPuerta() else None
        self.laberinto.recorrer(op)
    
    def cerrarPuerta(self,hab1,hab2):
        def op(x):
            return x.cerrar() if x.esPuerta() and (x.lado1.ref is hab1 or x.lado2.ref is hab1) and (x.lado1.ref is hab2 or x.lado2.ref is hab2) else None
        self.laberinto.recorrer(op)

    def lanzarBichos(self):
        juego = self
        self.fase.lanzarBichos(juego)

    def puedeLanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarHilo(bicho)
    
    def agregarBicho(self, unBicho):
        unBicho.juego = self
        self.bichos.append(unBicho)
        unBicho.numero_identificador = len(self.bichos)

    def lanzarHilo(self, bicho):
        with self.lock:  
            if bicho.numero_identificador not in self.threads or not self.threads[bicho.numero_identificador].is_alive():
                th = threading.Thread(target=self.envoltura_actuar, args=(bicho,))
                th.start()
                self.agregarHilo(bicho, th)
            else:
                print(f"Ya existe un hilo bicho nº {bicho.numero_identificador}")

    def agregarHilo(self,bicho,hilo):
        self.threads[bicho.numero_identificador]=hilo

    def envoltura_actuar(self, bicho):
            try:
                bicho.actuar()
            except Exception as e:
                print(f"Error al actuar: {e}")
            finally:
                with self.lock:
                    if bicho.numero_identificador in self.threads:
                        del self.threads[bicho.numero_identificador]

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarModoSupersaiyan(self):
        return SuperSaiyan()
    
    def fabricarBicho(self):
        return Bicho()
    
    def fabricarBichoAgresivo(self,posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoAgresivo()

        bicho.corazones = 10
        bicho.poder = 3

        return bicho
    
    def fabricarBichoPerezoso(self,posicion):
        bicho = self.fabricarBicho()

        bicho.posicion = posicion
        bicho.modo = self.fabricarModoPerezoso()

        bicho.corazones = 10
        bicho.poder = 1

        return bicho
    
    def fabricarBichoSupersaiyan(self,posicion):
        bicho = self.fabricarBicho()

        bicho.posicion = posicion
        bicho.modo = self.fabricarModoSupersaiyan()

        bicho.corazones = 20
        bicho.poder = 10

        return bicho
    
    def fabricarPuerta(self):
        return Puerta()

    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        hab.putElementOn(self.fabricarNorte(), self.fabricarPared())
        hab.putElementOn(self.fabricarEste(), self.fabricarPared())
        hab.putElementOn(self.fabricarOeste(), self.fabricarPared())
        hab.putElementOn(self.fabricarSur(), self.fabricarPared())

        hab.addOr(self.fabricarNorte())
        hab.addOr(self.fabricarEste())
        hab.addOr(self.fabricarOeste())
        hab.addOr(self.fabricarSur())

        return hab

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
        return Veneno()
    
    def fabricarArco(self):
        print("Fabricando tu arco con poder")
        return Arco()
    
    def esJuego(self):
        return True

    def labAbstractFactory(self, obj):
        self.laberinto = self.fabricarLaberinto()

        hab1 = obj.fabricarHabitacion(1)
        hab2 = obj.fabricarHabitacion(2)
        hab3 = obj.fabricarHabitacion(3)
        hab4 = obj.fabricarHabitacion(4)

        p1 = obj.fabricarPuerta()
        p2 = obj.fabricarPuerta()
        p3 = obj.fabricarPuerta()
        p4 = obj.fabricarPuerta()

        p1.lado1= hab1
        p1.lado2= hab2

        p2.lado1= hab2
        p2.lado2= hab4

        p3.lado1 = hab4
        p3.lado2 = hab3

        bomba = obj.fabricarBomba()
        bomba.componentes = p3

        p4.lado1 = hab3
        p4.lado2 = hab1

        otraBomba = obj.fabricarBomba()

        hab1.putElementOn(obj.fabricarEste(), p1)
        hab1.putElementOn(obj.fabricarSur(), p4)

        hab2.putElementOn(obj.fabricarOeste(), p1)
        hab2.putElementOn(obj.fabricarSur(), p2)


        hab3.putElementOn(obj.fabricarNorte(), p4)
        hab3.putElementOn(obj.fabricarEste(), bomba)

        hab4.putElementOn(obj.fabricarNorte(), p2)
        hab4.putElementOn(obj.fabricarOeste(), otraBomba)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        primerBicho = obj.fabricarBichoPerezoso(hab1)
        segundoBicho = obj.fabricarBichoAgresivo(hab2)
        self.agregarBicho(primerBicho)
        self.agregarBicho(segundoBicho)

    def nuevoLaberinto(self):
        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        p1 = self.fabricarPuerta()
        p2 = self.fabricarPuerta()
        p3 = self.fabricarPuerta()
        p4 = self.fabricarPuerta()

        p1.lado1= hab1
        p1.lado2= hab2

        p2.lado1= hab2
        p2.lado2= hab4

        p3.lado1 = hab4
        p3.lado2 = hab3

        bomba = self.fabricarBomba()
        bomba.componentes = p3

        p4.lado1 = hab3
        p4.lado2 = hab1

        otraBomba = self.fabricarBomba()

        hab1.ponerElementoEn(self.fabricarEste(),p1)
        hab1.ponerElementoEn(self.fabricarSur(),p4)

        hab2.ponerElementoEn(self.fabricarOeste(),p1)
        hab2.ponerElementoEn(self.fabricarSur(),p2)

        hab3.ponerElementoEn(self.fabricarNorte(),p4)
        hab3.ponerElementoEn(self.fabricarEste(), bomba)

        hab4.ponerElementoEn(self.fabricarNorte(), p2)
        hab4.ponerElementoEn(self.fabricarOeste(), otraBomba)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        bicho1 = self.fabricarBichoPerezoso(hab1)
        bicho2 = self.fabricarBichoAgresivo(hab2)
        self.agregarBicho(bicho1)
        self.agregarBicho(bicho2)


    def laberinto2HabFM(self):

        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta()

        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        hab1.norte= self.fabricarPared()
        hab1.este= self.fabricarPared()
        hab1.oeste= self.fabricarPared()

        hab2.este= self.fabricarPared()
        hab2.oeste= self.fabricarPared()
        hab2.sur= self.fabricarPared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2Hab(self):
        self.laberinto = Laberinto()

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta = Puerta()

        hab1.sur = puerta
        hab2.norte = puerta

        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.norte= Pared()
        hab1.este= Pared()
        hab1.oeste= Pared()

        hab2.este= Pared()
        hab2.oeste= Pared()
        hab2.sur= Pared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)