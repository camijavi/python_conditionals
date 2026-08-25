from Components import clearConsole 

def storeCredit():
    clearConsole()
    registered = input("¿El cliente está registrado? (Si/No): ").strip().lower()

    if registered == "si":
        balance = float(input("Ingrese el saldo del cliente: "))
        if balance > 500:
            return "Venta denegada: Su crédito supera los C$ 500"
        else:
            return "¡Venta aprobada!"
    else:
        return "Venta denegada: El cliente no está registrado en la pulpería"

def deliveryService():
    clearConsole()
    zone = input("Ingrese la zona de entrega (Urbana/Rural): ").strip().lower()

    if zone == "urbana":
        weight = float(input("Ingrese el peso del paquete en kg: "))
        if weight > 5:
            rate = 80.0
            return f"Zona Urbana (Paquete > 5 kg): La tarifa de envío es C$ {rate:.2f}"
        else:
            rate = 50.0
            return f"Zona Urbana (Paquete <= 5 kg): La tarifa de envío es C$ {rate:.2f}"
    elif zone == "rural":
        weight = float(input("Ingrese el peso del paquete en kg: "))
        if weight > 5:
            rate = 150.0
            return f"Zona Rural (Paquete > 5 kg): La tarifa de envío es C$ {rate:.2f}"
        else:
            rate = 100.0
            return f"Zona Rural (Paquete <= 5 kg): La tarifa de envío es C$ {rate:.2f}"
    else:
        return "Zona no válida. Ingrese 'Urbana' o 'Rural'."

def coffeeGrading():
    #     Clasificación de café
#     Tu misión: Una cooperativa primero verifica si la humedad está entre 10% y 12%. Si cumple,
#      clasifica el lote según los defectos reportados. Propón categorías claras.
#     Pista: La segunda decisión depende de la primera.
    clearConsole()

def accommodationBooking():
    #    Tu misión: Un hospedaje de Granada ofrece una promoción simulada en temporada baja.
#     Dentro de esa temporada, el porcentaje depende de si la reserva alcanza 3 noches.
#    Pista: Evalúa la duración dentro de temporada baja.
    clearConsole()

def hardwareSales():
    #    Tu misión: Una ferretería distingue mayoristas y minoristas. Para cada tipo, el descuento
#     depende de un monto mínimo diferente. Propón porcentajes y explica tus reglas.
#    Pista: Primero decide el tipo de cliente.
    clearConsole()
