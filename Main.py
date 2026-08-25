from SimpleIf import (
    cornerstoreStockManagement,
    storePromotion,
    salesGoal,
    diningRoomSetDelivry,
    productWeight
)
from NestedIf import (
    storeCredit,
    deliveryService,
    coffeeGrading,
    accommodationBooking,
    hardwareSales
)
from UI import showMainMenu, showSimpleIfMenu, showNestedIfMenu


def handleSimpleIf():
    while True:
        option = showSimpleIfMenu()
        match option:
            case "1":
                print("\n" + cornerstoreStockManagement())
            case "2":
                print("\n" + storePromotion())
            case "3":
                print("\n" + salesGoal())
            case "4":
                print("\n" + diningRoomSetDelivry())
            case "5":
                print("\n" + productWeight())
            case "0":
                break
            case _:
                print("\nOpción no válida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")


def handleNestedIf():
    while True:
        option = showNestedIfMenu()
        match option:
            case "1":
                print("\n" + storeCredit())
            case "2":
                print("\n" + deliveryService())
            case "3":
                print("\n" + coffeeGrading())
            case "4":
                print("\n" + accommodationBooking())
            case "5":
                print("\n" + hardwareSales())
            case "0":
                break
            case _:
                print("\nOpción no válida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")


def main():
    while True:
        choice = showMainMenu()
        match choice:
            case "1":
                handleSimpleIf()
            case "2":
                handleNestedIf()
            case "0":
                print("\n¡Gracias por utilizar el sistema! Hasta luego.\n")
                break
            case _:
                print("\nOpción no válida. Intente de nuevo.")
                input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()