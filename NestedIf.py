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
    clearConsole()
    humidity = float(input("Ingrese el porcentaje de humedad del café: "))

    if 10 <= humidity <= 12:
        defects = int(input("Ingrese la cantidad de defectos por cada 100 gramos: "))
        if defects == 0:
            return "Calidad Premium: El café cumple con la humedad requerida y no tiene defectos."
        elif 1 <= defects <= 5:
            return "Calidad Estándar: El café cumple con la humedad requerida y tiene pocos defectos."
        elif 6 <= defects <= 15:
            return "Calidad Comercial: El café cumple con la humedad requerida pero excede el límite de defectos."
        else:
            return "Calidad No Conforme: El café no cumple con los estándares de calidad debido a la alta cantidad de defectos."
    else:
        return "Humedad no conforme: El café no cumple con el rango de humedad requerido (10% - 12%)"


def accommodationBooking():
    clearConsole()
    season = input("¿Es temporada baja? (Si/No): ").strip().lower()

    if season == "si":
        nights = int(input("Ingrese el número de noches reservadas: "))
        if nights >= 3:
            return "Promoción especial aplicada: Obtienes un 20% de descuento por reservar más de 3 noches en temporada baja."
        else:
            return "Promoción no aplicada: No cumples con los requisitos para la promoción de temporada baja."
    else:
        return "No hay promoción disponible, ya que no es temporada baja."


def hardwareSales():
    clearConsole()

    clienType= input("¿Es mayorista o minorista? (Mayorista/Minorista): ").strip().lower()
    amount = float(input("Ingrese el monto de la compra: "))

    if clienType== "mayorista":
        if amount >= 2000:
            discount = amount * 0.15  # 15% de descuento
            total = amount - discount
            return f"Mayorista con compra >= C$ 2000: Se aplica un 15% de descuento. Total a pagar: C$ {total:.2f}"
        elif amount >= 1000:
            discount = amount * 0.10  # 10% de descuento
            total = amount - discount
            return f"Mayorista con compra >= C$ 1000: Se aplica un 10% de descuento. Total a pagar: C$ {total:.2f}"
        else:
            return f"Mayorista sin descuento: Su compra no alcanza el mínimo requerido de C$ 1000."
    elif clienType== "minorista":
        if amount >= 500:
            discount = amount * 0.05  # 5% de descuento
            total = amount - discount
            return f"Minorista con compra >= C$ 500: Se aplica un 5% de descuento. Total a pagar: C$ {total:.2f}"
        else:
            return f"Minorista sin descuento: Su compra no alcanza el mínimo requerido de C$ 500."
    else:
        return "Tipo de cliente no reconocido. Por favor ingrese 'Mayorista' o 'Minorista'."
