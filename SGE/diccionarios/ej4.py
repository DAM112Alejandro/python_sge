i=0
print("Cuantos alumnos tienes: ")
valor=(int(input()))
alumno={}
listaAprobados=[]
listaSuspendidos=[]
notaMedia=0
while i<valor:
    alumno[i]={}
    alumno[i]["nombre"]=input("nombre")
    alumno[i]["nota"]=int(input("nota"))
    nombre=alumno[i]["nombre"]
    if nota>=5:
        listaAprobados.append(nombre)
    else:
        listaSuspendidos.append(nombre)
    notaMedia+=nota
    i+=1
print(alumno)
print(listaAprobados)
print(listaSuspendidos)
print(notaMedia/i)