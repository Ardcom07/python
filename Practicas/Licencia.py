#Desarrollado por Alex
edad = int(input("Ingrese su edad: "))  # Convertir la entrada a entero

print(f"Usted tiene {edad} años")

if edad >= 18 and edad <= 60:
    print("Usted es mayor de edad. Licencia de Adulto")

elif edad >= 16 and edad < 18:
    print("Usted es menor de edad. Licencia de Menor")

else:
    print("Usted no puede tener aún licencia de conducir")
    print(f"Vuelva dentro de {16 - edad} años")  # Mostrar cuántos años le faltan
