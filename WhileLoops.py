from Components import clearConsole 

def cashClosing():
    clearConsole()

def systemAccess():
# Tu misión: Solicita la clave hasta que sea correcta. 
# Cuenta los intentos e informa cuántos fueron necesarios.

    clearConsole()
    print("INGRESE SUS CREDENCIALES")
    username = input("Usuario: ")
    loggedIn = False

    attempts = 0 

    while loggedIn != True:
        if  username == camijavi:
            password = input("Contraseña: ")
            if password == 123456:
                continue
            else:
                print("CONTRASEÑA INCORRECTA")
                attempts+= 1
        else:
            print("USUARIO INCORRECTA")
            attempts+= 1
            loggedIn = True
            print(f"BIENVENIDO DE VUELTA! {username}")


def orderQty():
    clearConsole()

def deliveryGas():
    clearConsole()

def stockReplenishment():
    clearConsole()