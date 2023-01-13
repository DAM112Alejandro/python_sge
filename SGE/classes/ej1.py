class robot:
    def __init__(self):
        self.x=0
        self.y=0

    def puesto_actual(self):
        return (self.x,self.y) 

    def mueve(self,letra):
        if letra.__eq__("A"):
            numero=int(input("Introduce el numero de casillas que se mueve hacia delante: "))
            self.y+=numero
        elif letra.__eq__("R"):
            numero=int(input("Introduce el numero de casillas que se mueve hacia atras: "))
            self.y-=numero
        elif letra.__eq__("I"):
            numero=int(input("Introduce el numero de casillas que se mueve hacia la izquierda: "))
            self.x-=numero
        elif letra.__eq__("D"):
            numero=int(input("Introduce el numero de casillas que se mueve hacia la derecha: "))
            self.x+=numero
        else:
            print("No existe este movimiento")
miRobot = robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    print(miRobot.puesto_actual())
               

