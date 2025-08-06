diccUsuarios = {"admin":"12345", "moises":"asdf"}

user = input("ingrese su usuario: ")
password = input("ingrese su contraseña: ")

intentos = 3 
if user in diccUsuarios:
    #usuario existente 
    intentos = intentos + 1 
    while intentos < 3: 
        if password == diccUsuarios[user]:
            print("Acceso correcto")
        else:
            print("Acceso incorrecto")
            intentos = intentos +1 
            password = input(f"intentos {intentos} de 3. Reescriba su contraseña: ")
else:

    print("Usuario no registrado")