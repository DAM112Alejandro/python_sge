lista=[1,345,2,22,524,2,5423,5,2,423,2,4,52]
diccionario={}

for i in lista:
    if i in diccionario:
        diccionario[i]=diccionario[i]+1
    else:
        diccionario[i]=1
print(lista)
print(diccionario)