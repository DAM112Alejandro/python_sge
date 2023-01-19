from random import randint, uniform,random

def func(numero):
    valor=int(input("Introduce un valor entre 1 y 10: "))
    while valor!=numero:
        if valor>numero:
            print(str(valor)+" es mayor que el que buscas")
            valor=int(input("Introduce un valor entre 1 y 10: "))
        else: 
            print(str(valor)+" es menor que el que buscas")
            valor=int(input("Introduce un valor entre 1 y 10: "))
    print("Has acertado")
        
      
func(randint(0,10))
