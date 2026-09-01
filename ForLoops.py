from Components import clearConsole 



def miniSuperSales():
    clearConsole()
    total = 0
    for d in range(1,8):
        venta = float(input("Ingrese la venta del día "))
        total += venta
    
    print("Total de la semana:", total)
    print("Promedio diario:", total/7)
    



def coffeeReception():
    clearConsole()
    totalWeight = 0.0

    print("Ingrese el peso de los sacos: ")
    for w in range(1,6):
        weight = float(input(f"Saco ({w}): "))
        totalWeight += weight
    return(f"El peso total de los 5 sacos es: {totalWeight} Lbs")


def stockChecking():
    clearConsole()

    lowStock = 0
    lowStockProducts = []

    print("Ingrese los datos solicitados: ")
    for p in range(1,9):
        productName = input(f"Nombre del producto ({p}): ")
        currentStock = int(input("Cantidad en existencia: "))

        if currentStock < 10:
            lowStockProducts.append(f"{productName} ({currentStock})")
    
    print ("Los siguientes productos tienen menos de 10 unidades en existencia: ")
    for stock in lowStockProducts:
        print (stock)
        
    return (f"Hay {len(lowStockProducts)} productos con una alerta de inventario bajo!")  # len is short for lenght. (counts and returns the number of items inside an object and that's what i need rn)





# def breadProduction():
#     # Una panadería registra durante 6 días la producción y las ventas.
#     # Calcula totales y producto sobrante.
#     clearConsole()

# def serviceEvaluation():
#     # Un restaurante recoge 10 calificaciones entre 1 y 5.
#     # Calcula el promedio y cuenta cuántas fueron 4 o 5.
#     clearConsole()
