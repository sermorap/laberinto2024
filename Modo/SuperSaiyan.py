from Modo.Modo import Modo

class SuperSaiyan(Modo):
    
    def atacar(self, unBicho):
        unBicho.atacar()

    def chetarse(self, unBicho):
        unBicho.set_corazones(unBicho.corazones + 100)
        print(f"El bicho ha obtenido {unBicho.corazones} corazones extra.")  
    
    def esSupersaiyan(self):
        return True
    
    def __str__(self):
        return "Modo SuperSaiyan ACTIVADO"
