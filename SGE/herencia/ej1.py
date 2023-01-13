class poligono:
    def __init__(self,color,lista):
        self.color=color
        self.lista=lista
    
    def perimetro(self):
        perimetro=0
        for i in self.lista:
            perimetro+=i
        print(perimetro)
    

class triangulo:
    def __init__(self,color,lista):
        poligono.__init__(self,color,lista)
    
    def perimetro(self):
        poligono.perimetro(self)
    
    def forma(self):

        if self.lista[0]==self.lista[1] and self.lista[0]==self.lista[2]:
            print("Es equilatero")
        elif self.lista[0]==self.lista[1] or self.lista[1]==self.lista[2] or self.lista[0]==self.lista[2]:
            print("Es isosceles")
        else:
            print("Es escaleno")

class cuadrado:
    def __init__(self,color,lista):
        poligono.__init__(self, color, lista)

    def perimtro(self):
        poligono.perimetro(self)

mitriangulo=triangulo("rojo",[1,2,3])
mitriangulo.perimetro()
mitriangulo.forma()
print(mitriangulo.__getattribute__("color"))

micuadrado=cuadrado("azul",[4,4,4,4])
micuadrado.perimtro()
print(micuadrado.__getattribute__("color"))
