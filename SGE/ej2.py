i=0
lista=[]
lista1=[]
lista2=[]
while i<5:
    numero=input("Escribe un numero: ")
    lista.append(numero)
    numero2=input("Escribe un numero: ")
    lista2.append(numero2)
    i+=1
for i in lista:
    if lista2.__contains__(i) and i not in lista1:
        lista1.append(i)
print(lista1)
print(lista)
print(lista2)

