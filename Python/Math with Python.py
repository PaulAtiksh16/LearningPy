##for x in range(1, 1000, 1):
##    if ((9*x + 2) - 92) == 0:
##        print(x)


##for x in range(1, 1000, 1):
##    if (6*x + 5) == 17:
##        print(x)


##for x in range(1, 1000, 1):
##    if (6*x - 5) == 49:
##        print(x)


##for x in range(1, 1000, 1):
##    if (x + 2) == 100:
##        print(x)


##for x in range(1, 1000, 1):
##    if (9*x) == 9:
##        print(x)


##for x in range(1, 1000, 1):
##    if (10*x-2*x) == 40:
##        print(x)


##for x in range(1, 1000, 1):
##    if (x/2 + x/2) == 10:
##        print(x)


# print("Give me a equation")
# equation = input()
# equation.split()
# oof = list(equation)
# oof.pop(1)
# oof.pop(2)
# if oof[1] == "+":
#     print(int(oof[0]) + int(oof[2]))
# if oof[1] == "*":
#     print(int(oof[0]) * int(oof[2]))
# if oof[1] == "/":
#     print(int(oof[0]) / int(oof[2]))
# if oof[1] == "-":
#     print(int(oof[0]) - int(oof[2]))


###start
##print("How many numbers?")
##length = int(input()) + 1
##numbers = []
##dicty = {}
##high = 0
##higher = 0
###mean
##for things in range(1, length, 1):
##    print("Give me a number!")
##    num = int(input())
##    numbers.append(num)
##    numbers.sort()
##mean = sum(numbers)/2
###median
##if len(numbers)%2 != 0:
##    half = len(numbers)//2
##    median = numbers[int(half)]
##else:
##    half = [int(len(numbers)/2 - 1), int(len(numbers)/2)]
##    half_one = half[0]
##    half_two = half[1]
##    median = (numbers[half_one] + numbers[half_two])/2
###mode
##for things in range(0, length - 1, 1):
##    if numbers[things] >= high:
##        high = numbers[things]
##for things in range(1, length - 1, 1):
##    dicty[numbers[things]] = 0
##for things in range(0, length - 1, 1):
##    dicty[numbers[things]] = dicty[numbers[things]] + 1
##for things in dicty:
##    if dicty[things] >= higher:
##        higher = things
##mode = higher
###print all
##print("Mean:", mean)
##print("Median:", median)
##print("Mode:", mode)


##import random
##count = 0
##five = 0
##for things in range(1, 7, 1):
##    for thoongs in range(1, 7, 1):
##        for ham in range(1, 7, 1):
##            if things + thoongs + ham == 5:
##                five = five + 1
##            count = count + 1
##print(str(100*(five/count)) + "%")
    

##import random
##count = 0
##oof = 0
##for things in range(1, 1000001, 1):
##    dice_one = random.randint(1, 6)
##    dice_two = random.randint(1, 6)
##    dice_three = random.randint(1, 6)
##    dice_four = random.randint(1, 6)
##    dice_five = random.randint(1, 6)
##    if (dice_one == 1) and (dice_two == 2) and (dice_three == 3) and (dice_four == 4) and (dice_five == 5):
##        oof = oof + 1
##    count = count + 1
##print(str(100*(oof/count)) + "%")


##import random
##count = 0
##alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
##for things in range(1, 1000001, 1):
##    goof = []
##    for oof in range(1, 4, 1):
##        aaa = random.choice(alphabet)
##        goof.append(aaa)
##    if (goof[0] == "c") and (goof[0] == "a") and (goof[0] == "t"):
##        count = count + 1
##print(str(100*(oof/1000001)) + "%")


# import random
# count = 0
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# for things in range(1, 1000001, 1):
#     goof = []
#     for oof in range(1, 3, 1):
#         aaa = random.choice(alphabet)
#         goof.append(aaa)
#     if (goof[0] == "n") and (goof[0] == "o"):
#         count = count + 1
# print(str(100*(oof/1000001)) + "%")


# #prime number calculator
# print("Give me a number!")
# number = int(input())
# barunga = None
# for things in range(1, number + 1, 1):
#     if (number%things == 0) and (things != number) and (things != 1):
#         barunga = False
# if barunga == False:
#     print("This number isn't prime!")
# else:
#     print("This is prime!")


# #factors calculator
# factors = []
# print("Give me a number!")
# number = int(input())
# for things in range(1, number + 1, 1):
#     if (number%things == 0) and (number not in factors):
#         factors.append(things)
# print(factors)


# #prime factors calculator
# factors = []
# print("Give me a number!")
# number = int(input())
# barunga = None
# aaa = 0
# yoda = []
# for things in range(1, number + 1, 1):
#     if (number%things == 0) and (number not in factors):
#         factors.append(things)
# for numbers in range(0, len(factors), 1):
#     for things in range(1, numbers + 1, 1):
#         if (numbers%things == 0) and (things != numbers) and (things != 1):
#             barunga = False
#     if barunga == False:
#         aaa = aaa + 1
#     else:
#         yoda.append(numbers)
# if 0 in yoda:
#     yoda.remove(0)
# print(yoda)


# print("Give me a number!")
# number = int(input())
# while True:
#     if number%2 == 0:
#         number = number/2
#     else:
#         number = (number * 3) + 1
#     if number == 1:
#         break
#     print(int(number))
# print(int(number))


# print("What's your balance?")
# balance = int(input())
# print("What's your type of interest?")
# typey = input()
# print("What's your interest percent?")
# percent = int(input())
# print("How many years?")
# years = int(input())

# #simple
# if typey == "simple":
#     total = (((percent/100) * balance) * years) + balance
#     print(total)

# #compound
# elif typey == "compound":
#     for things in range(1, years + 1, 1):
#         total = ((percent/100) * balance)
#         balance = balance + total
#     print(balance)


# print("How much was the meal?")
# meal = int(input())
# print("What is the tip percentage?")
# tip = int(input())
# print("What is the tax percentage?")
# tax = int(input())
# tip_cost = meal * (tip/100)
# tax_cost = meal * (tax/100)
# total = meal + tip_cost + tax_cost
# print("Tip:", tip_cost)
# print("Tax:", tax_cost)
# print("Total:", total)


# import math
# print("What do you need to calculate? (a, b, c)")
# side = input()
# if side == "c":
#     print("How long is side A?")
#     a = int(input())
#     print("How long is side B?")
#     b = int(input())
#     print(math.sqrt(a**2 + b**2))
# elif side == "a":
#     print("How long is side B?")
#     b = int(input())
#     print("How long is side C?")
#     c = int(input())
#     print(math.sqrt(c**2 - b**2))
# elif side == "b":
#     print("How long is side A?")
#     a = int(input())
#     print("How long is side C?")
#     c = int(input())
#     print(math.sqrt(c**2 - a**2))


# import math
# for a in range(1, 11, 1):
#     for b in range(1, 11, 1):
#         c = math.sqrt(a**2 + b**2)
#         if c == c//1:
#             print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(int(c)) + ".")
    

# import math    
# print("What is your shape? (rectangle, circle, triangle, trapezoid)")
# shape = input()
# if shape == "rectangle":
#     print("What is the height?")
#     height = int(input())
#     print("What is the width?")
#     width = int(input())
#     area = height * width
#     print(area)
# elif shape == "circle":
#     print("What is the radius?")
#     radius = int(input())
#     print("What do you use for pi? (For actual pi, type 'pi')")
#     pi = input()
#     if pi != "pi":
#         print((radius**2) * float(pi))
#     else:
#         print((radius**2) * math.pi)
# elif shape == "triangle":
#     print("What is the height?")
#     height = int(input())
#     print("What is the base?")
#     base = int(input())
#     print((base * height)/2)
# elif shape == "trapezoid":
#     print("What is the length of the top base?")
#     a = int(input())
#     print("What is the length of the bottom base?")
#     b = int(input())
#     print("What is the height?")
#     height = int(input())
#     print(((a + b)/2) * height)


# import math
# print("What is x?")
# x = int(input())
# print("What is y?")
# y = int(input())
# print("What is a?")
# a = int(input())
# print("What is b?")
# b = int(input())
# print(math.sqrt((x - a)**2 + (y - b)**2))








