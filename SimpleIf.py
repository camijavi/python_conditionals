from Components import clearConsole 

def cornerstoreStockManagement():
    clearConsole()
    productName = input("Ingrese el nombre del producto: ")
    currentStock = int(input("Ingrese el número de unidad que hay en existencia: "))

    if currentStock < 5:
        return "ADVERTENCIA: ¡Le quedan menos de 5 unidades en existencia!"
    else:
        return f"El producto {productName}, cuenta con {currentStock} unidades en existencia"
    


def storePromotion():
  clearConsole()

    

def salesGoal():
  clearConsole()


def diningRoomSetDelivry():
    clearConsole()


def productWeight():
    clearConsole()