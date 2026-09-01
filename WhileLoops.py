from Components import clearConsole 

def cashClosing():
    clearConsole()

    print("--- CIERRE DE CAJA ---")
    print("Ingrese el monto de cada venta (0 para finalizar):")
    salesCount = 0
    totalMoneyMade = 0
    while True:
        saleAmount = float(input("Monto de la venta: "))

        if saleAmount == 0:
            break
        else:
            totalMoneyMade += saleAmount
            salesCount += 1
    print(f"Total recaudado: ${totalMoneyMade:.2f}") 
    print(f"Total ventas realizadas: {salesCount}")        
    

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

    while True:
        qty = int(input("Ingrese la cantidad de unidades (1 - 100): "))
        

        if 1 <= qty <= 100:
            break  
        
        print("Error: La cantidad debe estar entre 1 y 100. Intente nuevamente.\n")

 
    unitPrice = float(input("Ingrese el precio por unidad: C$ "))
    total = qty * unitPrice

    return f"Pedido aprobado: {qty} unidades. Total a pagar: C$ {total:.2f}"



def deliveryGas():
    clearConsole()
    gas = 8.0
    while gas > 1:
        consumption = float(input("Registre el consumo del recorrido (litros): "))
        
        # Deduct consumption from current gas
        gas -= consumption
        if gas > 1:
            print(f"Combustible restante: {gas:.2f} litros\n")
    return "ALERTA: Le queda 1 litro."


def stockReplenishment():
    clearConsole()
    units = 3
    unitsGoal = 20
    print("--- REPOSICIÓN DE PRODUCTOS ---")
    while unitsGoal == units:
        units = int(input("Cantidad de unidades: "))
    return "SE HA ALCANZADO LA META"
