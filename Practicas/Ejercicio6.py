
caracter = input("Ingresa el caracter para dibujar (* o una letra): ")

tamaño = int(input("Ingresa el tamaño (entero positivo): "))

print("\nTriángulo rectángulo:")
for i in range(1, tamaño + 1):
    print(caracter * i)

print("\nCuadrado:")
for i in range(tamaño):
    print(caracter * tamaño)
