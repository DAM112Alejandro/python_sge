usuarios = {
 "iperurena": {
 "nombre": "Iñaki",
 "apellido": "Perurena",
 "password": "123123"
 },
 "fmuguruza": {
 "nombre": "Fermín",
 "apellido": "Muguruza",
 "password": "654321"
 },
 "aolaizola": {
 "nombre": "Aimar",
 "apellido": "Olaizola",
 "password": "123456"
 }
}

i=0
while i<3:
    usuario=(input("Introduce el usuario: "))
    contraseña=(input("Introduce una contraseña: "))
    if usuarios.__contains__(usuario):
        if contraseña==usuarios[usuario].get("password"):
            print(usuarios[usuario].get("nombre")+" "+usuarios[usuario].get("apellido"))
            break
    else:
        i+=1                                                        
