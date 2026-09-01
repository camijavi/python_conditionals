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
from ForLoops import (
    miniSuperSales,
    coffeeReception,
    stockChecking,
    breadProduction,
    serviceEvaluation
)

from WhileLoops import (
    cashClosing,
    systemAccess,
    orderQty,
    deliveryGas,
    stockReplenishment
)
from Components import invalidOptionMessage

from UI import showMainMenu, showSimpleIfMenu, showNestedIfMenu, showForLoopMenu, showWhileLoopMenu, pause


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
                invalidOptionMessage()
        pause()


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
               invalidOptionMessage()
        pause()

def handleForLoop():
    while True:
        option = showForLoopMenu()
        match option:
            case "1":
                print("\n" + miniSuperSales())
            case "2":
                print("\n" + coffeeReception())
            case "3":
                print("\n" + stockChecking())
            case "4":
                print("\n" + breadProduction())
            case "5":
                print("\n" + serviceEvaluation())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()

def handleWhileLoop():
    while True:
        option = showWhileLoopMenu()
        match option:
            case "1":
                print("\n" + cashClosing())
            case "2":
                print("\n" + systemAccess())
            case "3":
                print("\n" + orderQty())
            case "4":
                print("\n" + deliveryGas())
            case "5":
                print("\n" + stockReplenishment())
            case "0":
                break
            case _:
                invalidOptionMessage()
        pause()
    
def main():
    while True:
        choice = showMainMenu()
        match choice:
            case "1":
                handleSimpleIf()
            case "2":
                handleNestedIf()
            case "3":
                handleForLoop()
            case "4":
                handleWhileLoop()
            case "0":
                print("\n¡Gracias por utilizar el sistema! Hasta luego.\n")
                break
            case _:
                invalidOptionMessage()
                pause()


if __name__ == "__main__":
    main()