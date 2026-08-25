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
#     Tu misión: Un emprendimiento calcula una tarifa simulada según zona urbana o rural y,
#      dentro de cada zona, según si el paquete supera 5 kg. Propón tarifas y calcula el total.
#     Pista: Decide primero la zona y después el peso.
    clearConsole()

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
