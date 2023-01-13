class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ordenes = []
        self.historial = []

 

    def mueve(self, orden):
        for i in orden:
            self.ordenes.append(i)
            if i == 'A':
                self.y += 1
            elif i == 'D':
                self.x += 1
            elif i == 'I':
                self.x -= 1
            elif i == 'R':
                self.y -= 1
            else:
                print('Orden no válida')
            self.historial.append((self.x,self.y))
    def ordenes_recibidas(self):
        return self.ordenes
    def volver_inicio(self):
        ruta = []
        for i in range(len(self.historial)-1):
            ruta.append(self.historial[i])
        return ruta
robot = Robot()
robot.mueve("AADDADIR")
print(robot.ordenes_recibidas()) # imprime ['A', 'A', 'D', 'D', 'A', 'D', 'I', 'R']
print(robot.volver_inicio()) #imprime [(0,0),(0,1),(1,1),(1,2),(1,1),(1,0),(0,0)]