from Components import clearConsole

def drawHeader(title):
    print("=" * 55)
    print(f"{title.center(55)}")
    print("=" * 55)

def showMainMenu():
    clearConsole()
    drawHeader("SISTEMA DE EJERCICIOS CONDICIONALES")
    print(" [1] Ejercicios con 'If Simples'")
    print(" [2] Ejercicios con 'If Anidados'")
    print(" [0] Salir")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()

def showSimpleIfMenu():
    clearConsole()
    drawHeader("EJERCICIOS: IF SIMPLES")
    print(" [1] Control de Existencias de Pulpería")
    print(" [2] Promoción de Tienda (Descuento)")
    print(" [3] Cumplimiento de Meta de Ventas")
    print(" [4] Envío de Juego de Comedor")
    print(" [5] Verificación de Peso de Producto")
    print(" [0] Volver al Menú Principal")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()

def showNestedIfMenu():
    clearConsole()
    drawHeader("EJERCICIOS: IF ANIDADOS")
    print(" [1] Crédito de Pulpería")
    print(" [2] Servicio de Entrega (Urbana / Rural)")
    print(" [3] Clasificación de Calidad de Café")
    print(" [4] Reserva de Hospedaje en Granada")
    print(" [5] Ventas de Ferretería (Mayorista / Minorista)")
    print(" [0] Volver al Menú Principal")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()
