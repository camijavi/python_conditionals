from Components import clearConsole 

def cornerstoreStockManagement():
    clearConsole()
    registered = input("¿El cliente está registrado? (Si/No): ").strip().lower()

    if registered == "no":
        return "Venta denegada: El cliente no está registrado en la pulpería"
    
    balance = float(input("Ingrese el saldo del cliente: "))
    
    if balance > 500:
        return "Venta denegada: Su crédito supera los C$ 500"
    else: 
        return "¡Venta aprobada!"




    

def storePromotion():
    discount = 100

def salesGoal():
    lala = ""

def diningRoomSetDelivry():
    lala = "123"

def productWeight():
    lala = "lala"