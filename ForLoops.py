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


# def stockChecking():
#     # Una distribuidora revisa 8 productos.
#     # Solicita nombre y existencia; muestra los que
#     # tienen menos de 10 unidades y cuenta las alertas.
#     clearConsole()

# def breadProduction():
#     # Una panadería registra durante 6 días la producción y las ventas.
#     # Calcula totales y producto sobrante.
#     clearConsole()

# def serviceEvaluation():
#     # Un restaurante recoge 10 calificaciones entre 1 y 5.
#     # Calcula el promedio y cuenta cuántas fueron 4 o 5.
#     clearConsole()
