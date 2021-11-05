def getAppleCost():
    appleQuantity = int(input("How many apples will you buy? "))
    applePrice = 20
    _appleTotalCost =int(appleQuantity * applePrice)
    return _appleTotalCost
    
def getOrangeCost():
    orangeQuantity = int(input("How many oranges will you buy? "))
    orangePrice = 25
    _orangeTotalCost = int(orangeQuantity * orangePrice)
    return _orangeTotalCost

def totalAmount(_apples, _oranges):
    _total = int(_apples + _oranges)
    return _total

def display(totalJ):
    print(f'The total amount is {totalJ}')

apples = getAppleCost()
oranges = getOrangeCost()
total = totalAmount(apples, oranges)
display = display(total)