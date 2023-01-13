def esPrimo(num):
    for i in range(2,num):
        if (num%i) == 0:
            return False
    return True 

if(esPrimo(int(input("Introduce un numero")))):
    print("Es primo")
else:
    print("No es primo")