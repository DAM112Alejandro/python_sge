file = open("fichero.txt", "a")
resultado=0
while True:
    sumandos=int(input("Introduce un numero: "))
    file.write(str(sumandos)+"+")
    resultado+=sumandos
    seguir=input("Quieres continuar: y / n")
    if seguir.__eq__("y"):
        True
    else:
        file.write("0="+str(resultado))
        break
        


