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





def breadProduction():
    clearConsole()
    overstock = 0
    totalSold = 0
    totalMade = 0
    for days in range(1,7):
        print(f"DÍA [{days}]")

        qtyMade= int(input("Cantida de productos hechos: "))
        qtySold = int(input("Cantidad de productos vendidos: "))
        
        totalMade += qtyMade
        totalSold += qtySold
    
    overstock = totalMade - totalSold
    print(f"Total hecho {totalMade}")
    print(f"Total vendido {totalSold}")
    print(f"Sobrantes {overstock}")


def serviceEvaluation():
    clearConsole()
    total = 0
    highRating = 0
    ratingAverage = 0.0
    print("Ingrese una calificación (★ 1- 5) ")
    for r in range(1,11):
        restaurantRating = int(input(f"★ Calificación ({r}): "))
        total += restaurantRating

        if restaurantRating >= 4:
            highRating += 1
    ratingAverage = total / 10
    print(f"★ Promedio de las calificaciones: {ratingAverage}")
    print(f"★ Total de calificaciones entre 4 y 5: {highRating}")