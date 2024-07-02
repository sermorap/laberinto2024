from ElementoMapa.Container.Container import Container

class Habitacion(Container):

    def entrar(self, obj):
        obj.setPosicion(self)
        print("Usted esta en ------>",self.ref)
    
    def aceptar(self, vst):
        print("Visitar habitación ", str(self.num))
        vst.visitarHabitacion(self)
        for ch in self.objChildren:
            ch.aceptar(vst)
        self.form.aceptar(vst)

    def esHabitacion(self):
        return True
    
    def __str__(self):
        info= "Habitación " + str(self.ref) +" donde " + str(self.form) 
        
        if len(self.objChildren)>0:
            dt = info + "\n [DETALLE HIJOS]:"
            for n in self.objChildren:
                dt = dt + "\n["+str(n)+"]"
        return dt