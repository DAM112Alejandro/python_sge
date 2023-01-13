class coche:
    def __init__(self,matricula,marca,kilometros_recorridos,gasolina):
        self.matricula=matricula
        self.marca=marca
        self.kilometros_recorridos=kilometros_recorridos
        self.gasolina=gasolina
    
    def avanzar(self, kilometros_a_conducir):
        self.kilometros_recorridos+=kilometros_a_conducir
        self.gasolina-=float(kilometros_a_conducir)*0.1
        if self.gasolina<0:
            print("Tienes que repostar")
        else:
            print(str(self.kilometros_recorridos),str(self.gasolina))
    
    def repostar(self,litros):
        self.gasolina+=float(litros)


micoche=coche("e","e",0,50.1)
micoche.avanzar(500)
micoche.repostar(20)
micoche.avanzar(100)
