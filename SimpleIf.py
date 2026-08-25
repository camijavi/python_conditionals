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
    totalSold = float(input("Ingrese el total vendido el día de hoy: "))

    if totalSold > 4000:
        return f"ÉXITO: Se superó la meta diaria.\nEl día de hoy se alcanzaron C$ {totalSold:.2f}"
    elif totalSold == 4000:
        return "ÉXITO: Se logró llegar a la meta diaria de C$ 4000.00"
    else:
        missing = 4000 - totalSold
        return f"No se logró la meta diaria. Faltaron C$ {missing:.2f} para cumplir la meta"


def diningRoomSetDelivry():
    clearConsole()

    delivery = float(input("Ingrese el monto de la entrega: "))

    if delivery >= 300:
        return f"La compra es mayor de C$ 300. El envío es totalmente gratis"
    else:
        surcharge = delivery + 40 
        return f"La compra es menor de C$ 300. Su total a pagar es de C$ {surcharge}, por el envío"
 

def productWeight():
    clearConsole()

    weight = float(input("Ingrese el peso del saco: "))

    if weight < 46:
        return "El peso del saco está por debajo del peso esperado (46 Kg)."
    else:
        return "El peso de este saco cumple con el peso esperdo (46kg)"
