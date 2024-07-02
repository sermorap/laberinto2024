import time
from abc import abstractmethod

class Modo():
    
    def actua(self,unBicho):
        self.caminar(unBicho)
        self.atacar(unBicho)
        self.chetarse(unBicho)
        self.dormir()

    def dormir(self):
        print('Bicho sobando JEJE')
        time.sleep(2)

    def caminar(self,unBicho):
        posicion = unBicho.obtener_orientacion_aleatoria()
        unBicho.irA(posicion)

    @abstractmethod
    def atacar(self,unBicho):
        pass

    @abstractmethod
    def chetarse(self,unBicho):
        pass

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def esSupersaiyan(self):
        return False