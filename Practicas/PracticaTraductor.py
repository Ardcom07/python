import time 
import os 
traductorSpEn = {"Hola":"Hello", "Adios": "Bye"}


while True:
    palabra = input("Traducir: ")

    if palabra != "0":
        if palabra in traductorSpEn:
            print(f"Españo\t| ")