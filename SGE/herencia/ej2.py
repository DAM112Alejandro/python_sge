class vehiculo:
    def __init__(self,kilometros):
        self.kilometros=kilometros
    
    def avanzar(self, kilometros_a_conducir):
        self.kilometros+=kilometros_a_conducir
    
class coche:
    def __init__(self,kilometros,gasolina):
        vehiculo.__init__(self,kilometros)
        self.gasolina=gasolina
    
    def avanzar(self, kilometros_a_conducir):
        vehiculo.avanzar(self, kilometros_a_conducir)
        self.gasolina-=float(kilometros_a_conducir)*0.1
        if self.gasolina<0:
            print("Tienes que repostar")
        else:
            print(str(self.kilometros),str(self.gasolina))
    
    def repostar(self,litros):
        self.gasolina+=float(litros)

class bici:
    def __init__(self,kilometros):
        vehiculo.__init__(self,kilometros)
    
    def avanzar(self,kilometros_a_conducir):
        vehiculo.avanzar(self, kilometros_a_conducir)
        if self.kilometros>=50:
            bici.hinchar_ruedas(self)
            print(str(self.kilometro))
        else:
            print(str(self.kilometros))
    
    def hinchar_ruedas(self):
        self.kilometro=0
    
micoche=coche(0,20)
micoche.avanzar(100)
micoche.repostar(20)
micoche.avanzar(300)

mibici=bici(0)
mibici.avanzar(40)
mibici.avanzar(60)
