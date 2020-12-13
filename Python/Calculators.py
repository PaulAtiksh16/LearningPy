import math
print("Which calculator would you like to use? (distance between points (point distance), shapes, pythagorean triples (pyth trip), pythagorean theorem (pyth theo), food, simple, prime, factors, balance, prime factors(pf))")
calc = input()

#prime number calculator
if (calc == "prime") or (calc == "Prime"):
    print("Give me a number!")
    number = int(input())
    barunga = None
    for things in range(1, number + 1, 1):
        if (number%things == 0) and (things != number) and (things != 1):
            barunga = False
    if barunga == False:
        print("This number isn't prime!")
    else:
        print("This is prime!")

#factors calculator
elif (calc == "factors"):
    factors = []
    print("Give me a number!")
    number = int(input())
    for things in range(1, number + 1, 1):
        if (number%things == 0) and (number not in factors):
            factors.append(things)
    if 0 in factors:
        factors.remove(0)
    print(factors)
    
#prime factors calculator
elif calc == "pf":
    factors = []
    print("Give me a number!")
    number = int(input())
    barunga = None
    aaa = 0
    yoda = []
    for things in range(1, number + 1, 1):
        if (number%things == 0) and (number not in factors):
            factors.append(things)
    for numbers in range(0, len(factors), 1):
        for things in range(1, numbers + 1, 1):
            if (numbers%things == 0) and (things != numbers) and (things != 1):
                barunga = False
        if barunga == False:
            aaa = aaa + 1
        else:
            yoda.append(numbers)
    if 0 in yoda:
        yoda.remove(0)
    print(yoda)

#balance calculator
elif calc == "balance":
    print("What's your balance?")
    balance = int(input())
    print("What's your type of interest?")
    typey = input()
    print("What's your interest percent?")
    percent = int(input())
    print("How many years?")
    years = int(input())
    
    #simple
    if typey == "simple":
        total = (((percent/100) * balance) * years) + balance
        print("Your balance after", str(years), "years will be $" + str(total) + ".")
    
    #compound
    elif typey == "compound":
        for things in range(1, years + 1, 1):
            total = ((percent/100) * balance)
            balance = balance + total
        print("Your balance after", str(years), "years will be $" + str(balance) + ".")

#very simple calculator
elif calc == "simple":
    print("Give me an equation. (Put spaces in between)")
    equation = input()
    equation.split()
    oof = list(equation)
    oof.pop(1)
    oof.pop(2)
    if oof[1] == "+":
        print(int(oof[0]) + int(oof[2]))
    if oof[1] == "*":
        print(int(oof[0]) * int(oof[2]))
    if oof[1] == "/":
        print(int(oof[0]) / int(oof[2]))
    if oof[1] == "-":
        print(int(oof[0]) - int(oof[2]))

#food calculator
elif calc == "food":
    print("How much was the meal?")
    meal = int(input())
    print("What is the tip percentage?")
    tip = int(input())
    print("What is the tax percentage?")
    tax = int(input())
    tip_cost = meal * (tip/100)
    tax_cost = meal * (tax/100)
    total = meal + tip_cost + tax_cost
    print("Tip:", tip_cost)
    print("Tax:", tax_cost)
    print("Total:", total)

#pythagorean theorem calculator
elif calc == "pyth theo":
    print("What do you need to calculate? (a, b, c)")
    side = input()
    if side == "c":
        print("How long is side A?")
        a = int(input())
        print("How long is side B?")
        b = int(input())
        print(math.sqrt(a**2 + b**2))
    elif side == "a":
        print("How long is side B?")
        b = int(input())
        print("How long is side C?")
        c = int(input())
        print(math.sqrt(c**2 - b**2))
    elif side == "b":
        print("How long is side A?")
        a = int(input())
        print("How long is side C?")
        c = int(input())
        print(math.sqrt(c**2 - a**2))

#pythagorean triples calculator
elif calc == "pyth trip":
    for a in range(1, 11, 1):
        for b in range(1, 11, 1):
            c = math.sqrt(a**2 + b**2)
            if c == c//1:
                print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(int(c)) + ".")

#shape calculator
elif calc == "shapes":
    print("What is your shape? (rectangle, circle, triangle, trapezoid)")
    shape = input()
    if shape == "rectangle":
        print("What is the height?")
        height = int(input())
        print("What is the width?")
        width = int(input())
        area = height * width
        print(area)
    elif shape == "circle":
        print("What is the radius?")
        radius = int(input())
        print("What do you use for pi? (For actual pi, type 'pi')")
        pi = input()
        if pi != "pi":
            print((radius**2) * float(pi))
        else:
            print((radius**2) * math.pi)
    elif shape == "triangle":
        print("What is the height?")
        height = int(input())
        print("What is the base?")
        base = int(input())
        print((base * height)/2)
    elif shape == "trapezoid":
        print("What is the length of the top base?")
        a = int(input())
        print("What is the length of the bottom base?")
        b = int(input())
        print("What is the height?")
        height = int(input())
        print(((a + b)/2) * height)

#distance between points calculator
elif calc == "point distance":
    print("What is x?")
    x = int(input())
    print("What is y?")
    y = int(input())
    print("What is a?")
    a = int(input())
    print("What is b?")
    b = int(input())
    print(math.sqrt((x - a)**2 + (y - b)**2))
    