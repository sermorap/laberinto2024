from Artefactos.Artefacto import Artefacto

class BolsilloMagico(Artefacto):
    
    def __init__(self):
        super().__init__()
        self.capacidad = 5
        self.children = []
        self.obsBolsillo = []

    def esBolsillo(self):
        return True
    
    def entrar(self, o):
        pass

    def usar(self, o):
        pass

    def expulsar(self, o):

        o.ref = None
        self.children.remove(o)

        for observadores in self.obsBolsillo:
                observadores.getBolsillo(self)

    def addArtefacto(self, art):

        if len(self.children) < self.capacidad:
            art.ref = self

            self.children.append(art)

            for observador in self.obsMochila:
                observador.visualmochila(self)
        else:
            print("*[¡!] Capacidad insuficiente en el bolsillo mágico de doraemon...*")

    def usado(self, ch):

        self.children.remove(ch)
        ch.ref = None
        for o in self.obsBolsillo:
                o.visualmochila(self)


    def getCommand(self, sj):
        setCommands = []
        setCommands.extend(self.commands)

        for hijo in self.children:
            setCommands.extend(hijo.getCommand(sj))

        return setCommands
    
    def observarBolsillo(self, ob):
        self.obsBolsillo.append(ob)

    def soltarArtefacto(self, art):
        self.children.remove(art)

        for obs in self.obsMochila:
            obs.visualmochila(self)

    def recorrer(self, sbj):
        sbj(self)
        map(sbj, self.children)

    def aceptar(self, vst):
        vst.visitarMochila(self)