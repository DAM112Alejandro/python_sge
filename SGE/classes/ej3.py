import math


class triangulo:

    def __init__(self,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3
    
    def area(self):
        s=int(self.l1+self.l2+self.l3)
        return math.sqrt(triangulo.perimetro(self) * (s - int(self.l1)) * (s - int(self.l2)) * (s - int(self.l3)))

    def perimetro(self):
        return self.l1+self.l2+self.l3
    
    def forma(self):
        if self.l1==self.l2 and self.l1==self.l3:
            print("Es equilatero")
        elif self.l1==self.l2 or self.l2==self.l3 or self.l1==self.l3:
            print("Es isosceles")
        else:
            print("Es escaleno")

mitriangulo=triangulo(1,2,3)
print(mitriangulo.perimetro())
print(mitriangulo.area())
print(mitriangulo.forma())