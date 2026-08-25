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
    sale = float(input("Ingrese el monto de la venta: "))

    if sale > 1500:
        discount = sale * 0.10 
        total = sale - discount
        return f"Su compra supera los C$ 1500. Se le aplicó un descuento del 10%\nEl total a pagar es C$ {total:.2f}"
    else:
        return "No se le puede aplicar descuento. Su compra no supera los C$1500"
    

def salesGoal():
  clearConsole()


def diningRoomSetDelivry():
    clearConsole()


def productWeight():
    clearConsole()