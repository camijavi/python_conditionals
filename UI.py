from Components import (clearConsole, menuFooter)

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
    menuFooter()

def showNestedIfMenu():
    clearConsole()
    drawHeader("EJERCICIOS: IF ANIDADOS")
    print(" [1] Crédito de Pulpería")
    print(" [2] Servicio de Entrega (Urbana / Rural)")
    print(" [3] Clasificación de Calidad de Café")
    print(" [4] Reserva de Hospedaje en Granada")
    print(" [5] Ventas de Ferretería (Mayorista / Minorista)")
    return menuFooter()

def showForLoopsfMenu():
    clearConsole()
    drawHeader("EJERCICIOS: BUCLES FOR")
    print(" [1] Ventas de un minisúper")
    print(" [2] Recepción de café")
    print(" [3] Revisión de inventario")
    print(" [4] Producción de pan")
    print(" [5] Evaluación del servicio")
    return menuFooter()

def showWhileLoopsMenu():
    clearConsole()
    drawHeader("EJERCICIOS: BUCLES WHILE")
    print(" [1] Cierre de caja")
    print(" [2] Acceso al sistema")
    print(" [3] Cantidad de un pedido")
    print(" [4] Combustible de reparto")
    print(" [5] Reposición de existencias")
    return menuFooter()
