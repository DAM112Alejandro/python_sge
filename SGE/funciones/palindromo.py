def esPalindromo(palabra: str):
    if palabra.upper() == palabra[::-1].upper():
        return True
    return False

print(esPalindromo(input("Introduce una palabra: ")))