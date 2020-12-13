##def salestax():
##    print("What is the price?")
##    price = int(input())
##    print("What is the tax percentage?")
##    tax = float(input())
##    total = price + price * (tax/100)
##    return(total)
##print(salestax())



print("How many pennies do you have?")
pennies = int(input())
def pennberg(pennies):
    pennymoney = pennies * 1
    return(pennymoney)
print("How many quarters do you have?")
quarters = int(input())
def quartberg(quarters):
    quartermoney = quarters * 25
    return(quartermoney)
print("How many dimes do you have?")
dimes = int(input())
def dimeberg(dimes):
    dimemoney = dimes * 10
    return(dimemoney)
print("How many nickels do you have?")
nickels = int(input())
def nickberg(nickels):
    nickelmoney = nickels * 5
    return(nickelmoney)
def totalmoney():
    total = pennberg(pennies) + quartberg(quarters) + dimeberg(dimes) + nickberg(nickels)
    return(total)
print(totalmoney())
