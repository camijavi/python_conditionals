from Components import clearConsole 

def cashClosing():
    clearConsole()

def systemAccess():
    clearConsole()
    print("INGRESE SUS CREDENCIALES")
    username = input("Usuario: ")
    loggedIn = False

    attempts = 0 

    while loggedIn != True:
        if  username == "camijavi":
            password = input("Contraseña: ")
            if password == "123456":
                loggedIn = True
                print(f"BIENVENIDO DE VUELTA! {username}")
            else:
                print("CONTRASEÑA INCORRECTA")
                attempts+= 1
        else:
            print("USUARIO INCORRECTA")
            attempts+= 1
    return(f"Se necesitaron {attempts} intentos para iniciar sesión")


def orderQty():
    clearConsole()

def deliveryGas():
    clearConsole()

def stockReplenishment():
    clearConsole()