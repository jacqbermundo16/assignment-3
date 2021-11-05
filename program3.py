# create prog that will ask amount of money
# will ask how much is an apple
# will compute max apples 
# diplay by the ff format 
# You can buy _ apples and your change is _ pesos

def getMoney():
    _money = int(input("How much money do you have? "))
    return _money

def getApplePrice():
    _apple = int(input("How much does a piece of apple costs? "))
    return _apple    

def getAppleMaxNo(_money, _apple):
    _appleMax = int(money // apple)
    return _appleMax

def computeAppleT(_apple, _appleM):
    _appleTotal = int(_apple * _appleM)
    return _appleTotal

def computeChange(_money, _appleT):
    _change = int(_money - _appleT)
    return _change   

def displayI(_appleM, _change):
    print(f"You can buy {_appleM} apples and your change is {_change} pesos.")

money = getMoney()
apple = getApplePrice()
appleM = getAppleMaxNo(money, apple)
appleT = computeAppleT(apple, appleM)
change = computeChange(money, appleT)
display = displayI(appleM, change)