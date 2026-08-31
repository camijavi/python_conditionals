import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def MenuFooter():
    print(" [0] Volver al Menú Principal")
    print("-" * 55)
    return input("Seleccione una opción: ").strip()