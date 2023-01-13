lista=[6,14,11,3,2,1,15,19]

def dentro_De(num):
    if(num<=20 and num>=1):
        return True
    return False


def enLista(num):
    if(dentro_De(num) and lista.__contains__(num)):
        return True
    return False

print(enLista(int(input("Introduce un numero: "))))