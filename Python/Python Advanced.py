##print("Give me a number")
##num = int(input())
##if num%5 == 0:
##    print("Super Squirter")
##else:
##    print("oof")


##print("Give me a string")
##num = input()
##if len(num) > 5:
##    print("Super Squirter")
##else:
##    print("oof")


##for bleh in range(1,16,1):
##    if bleh%2 != 0:
##        print(bleh)


####count = 0
####print(count)
####for bleh in range(1,12,1):
####    print(count + bleh)
####    oof = count + bleh
####    count = oof


##for things in range(1, 11, 1):
##    if things%2 == 0:
##        print(things - (2 * things))
##    else:
##        print(things)


##a = 5
##b = 6
##a, b = b, a
##print(a, b)


##for things in range(1, 10, 1):
##    if things%2 == 0:
##        print(10 * (things - (2 * things)))
##    else:
##        print(10 * things)
##print(100)

        
##print("What's your name?")
##name = input()
##for things in range (1, 11, 1):
##    if things != 5:
##        print(name)
##    else:
##        print("Hello")


##oof = 3
##for things in range(1, 5, 1):
##    print("*" * things)
##    print()
##for things in range(1, 4, 1):
##    print("*" * oof)
##    print()
##    oof = oof - 1


##oof = 6
##for things in range(1, 6, 1):
##    print("*" * oof)
##    print()
##    oof = oof - 1
##for things in range(1, 7, 1):
##    print("*" * things)
##    print()


##things = 1
##while things <= 10:
##    if things%2 == 0:
##        print(things - (2 * things))
##    else:
##        print(things)
##    things = things + 1


##nexts = 0
##first = 0
##second = 1
##print(nexts)
##print(1)
##for things in range(1, 12, 1):
##    nexts = first + second
##    print(nexts)
##    first = second
##    second = nexts
    

##up = True
##value = 1
##while True:
##    while up == True:
##        print(value)
##        value = value + 1
##        if value == 10:
##            up = False
##    while up == False:
##        print(value)
##        value = value - 1
##        if value == 1:
##            up = True
        

##oof = 1
##while oof <= 5:
##    print("Hello" + str(oof))
##    oof = oof + 1
    

##oof = 1
##while True:
##    print(oof)
##    oof = oof + 1
##    if oof == 11:
##        break


##oof = 0
##for things in range(1, 366, 1):
##    oof = oof + things
##print(2 * (oof - 84))


##for bleh in range(1, 4, 1):
##    space = 5
##    stars = 1
##    for things in range(1, 7, 1):
##        print(space * " " + stars * "*")
##        space = space - 1
##        stars = stars + 2
##for things in range(1, 11, 1):
##    print("     *")
    

##for bleh in range(1, 4, 1):
##    space = 0
##    stars = 11
##    for things in range(1, 7, 1):
##        print(space * " " + stars * "*")
##        space = space + 1
##        stars = stars - 2
##for things in range(1, 11, 1):
##    print("     *")


####board game
##one = 0
##two = 0
##import time
##import random
##print("P1|P2")
##while True:
##    dice_one = random.randint(1, 6)
##    dice_two = random.randint(1, 6)
##    if one + dice_one <= 100:
##        one = one + dice_one
##    if two + dice_two <= 100:
##        two = two + dice_two
##    for things in range(1, 101, 1):
##        if (one == things) and (two != things):
##            if things < 10:
##                if things%10 != 0:
##                    print(("P1" + "|"), end = "" )
##                else:
##                    print(("P1" + "|"), end = "" )
##                    print()
##            else:
##                if things%10 != 0:
##                    print(("P1" + "|"), end = "" )
##                else:
##                    print(("P1" + "|"), end = "" )
##                    print()
##        elif (two == things) and (one != things):
##            if things < 10:
##                if things%10 != 0:
##                    print(("P2" + "|"), end = "" )
##                else:
##                    print(("P2" + "|"), end = "" )
##                    print()
##            else:
##                if things%10 != 0:
##                    print(("P2" + "|"), end = "" )
##                else:
##                    print(("P2" + "|"), end = "" )
##                    print()
##        elif (two == things) and (one == things):
##            if things < 10:
##                if things%10 != 0:
##                    print(("BP" + "|"), end = "" )
##                else:
##                    print(("BP" + "|"), end = "" )
##                    print()
##            else:
##                if things%10 != 0:
##                    print(("BP" + "|"), end = "" )
##                else:
##                    print(("BP" + "|"), end = "" )
##                    print()
##        else:
##            if things < 10:
##                if things%10 != 0:
##                    print((str(things) + " |"), end = "" )
##                else:
##                    print((str(things) + "|"), end = "" )
##                    print()
##            else:
##                if things%10 != 0:
##                    print((str(things) + "|"), end = "" )
##                else:
##                    print((str(things) + "|"), end = "" )
##                    print()
##    if one == 100:
##        print("Player one wins!")
##        break
##    if (two == 100) and (one != 100):
##        print("Player two wins!")
##        break
##    print()
##    print("P1: " + str(one))
##    print("P2: " + str(two))
##    time.sleep(2)


##animals = ["cow", "lion", "dog", "frog"]
##sounds = ["moo", "roar", "woof", "ribbit"]
##for things in range(0, 4, 1):
##    print(animals[things], sounds[things])


##animals = ["cow", "lion", "dog", "frog", "duck", "horse"]
##for things in range(0, 6, 1):
##    if things%2 != 0:
##        print(animals[things])


##animals = ["cow", "lion", "dog", "frog", "duck", "horse"]
##for things in range(0, 6, 1):
##    if things%2 == 0:
##        print(animals[things])


##animals = ["cow", "lion", "dog", "frog", "duck", "horse"]
##animals.sort(reverse = True)
##for things in range(0, 6, 1):
##    print(animals[things])
##    print()


##import random
##oof = []
##for things in range(1, 31, 1):
##    aaa = random.randint(1, 200)
##    oof.append(aaa)
##print(oof)
##for thingoos in range(1, len(oof), 1):
##    if oof[thingoos]%2 == 0:
##        print(oof[thingoos])


##roomba = ["cow", "sheep", "pangolin", "blobfish", "minotaur", "dog", "fox", "bird", "cat", "penguin"]
##for things in range(1, len(roomba), 1):
##    if len(roomba[things]) > 5:
##        print(roomba[things])


##roomba = ["cow", "sheep", "pangolin", "blobfish", "minotaur", "dog", "fox", "bird", "abnormal", "penguin"]
##for things in range(1, len(roomba), 1):
##    if "a" in roomba[things] and "b" in roomba[things]:
##        print(roomba[things])


##aaa = 0
##oof = 0
##roomba = ["cow", "sheep", "pangolin", "blobfish", "minotaur", "dog", "fox", "bird", "abnormal", "penguin"]
##for things in range(1, len(roomba), 1):
##    if len(roomba[things]) > oof:
##        oof = len(roomba[things])
##        aaa = things
##print(roomba[aaa])


##animal_names = ["cow", "lion", "dog", "frog"]
##animal_sounds = ["moo", "roar", "woof", "ribbit"]
##animal_young = ["cowling", "cub", "puppy", "tadpole"]
##animals = [animal_names, animal_sounds, animal_young]
##for things in range(0, 4, 1):
##        print(animals[0][things], animals[1][things], animals[2][things])


##nums = [1,2,3,4,5]
##for things in range(0, len(nums), 1):
##  print(nums[things])


##nums = [1,2,3,4,5]
##for thingoo in range(1, 6, 1):
##    print(thingoo)
##    for things in range(0, len(nums), 1):
##        print(nums[things])


##nums = [1,2,3,4,5]
##for thingoo in range(1, 6, 1):
##    print(thingoo)
##    for things in range(0, len(nums), 1):
##        print(nums[things], end = "")
##    print()


##nums = [1,2,3,4,5]
##for things in range(0, len(nums), 1):
##    print(nums[things])
##    print(nums[things])


##nums = [1,2,3,4,5]
##for things in range(0, len(nums), 1):
##    print(str(nums[things]) * 2)


##nums = [6,7,8,9,10]
##for thingoo in range(1, 6, 1):
##    print(thingoo)
##    for things in range(0, len(nums), 1):
##        print(nums[things])


##a = [[[1, 2], [3, 4]]]
##b = [[[5, 6], [7, 8]]]
##print((a[0][0][0] + b[0][0][0]), (" "), (a[0][0][1] + b[0][0][0]))
##print((a[0][1][0] + b[0][1][0]), (a[0][1][1] + b[0][1][1]))


##import random
##aaa = []
##while True:
##    goo = random.randint(1, 10)
##    if goo not in aaa:
##        aaa.append(goo)
##    if len(aaa) == 10:
##        break
##print(aaa)


##import random
##cards = ["Jack of spades", "King of clubs", "Queen of hearts", "Ace of diamonds"]
##for things in range(1, 6, 1):
##    random.shuffle(cards)
##    print(cards)


##import random
##aaa = []
##while len(aaa) < 10:
##    goo = random.randint(1, 10)
##    if goo not in aaa:
##        aaa.append(goo)
##print(aaa)



##dicty = {"cow":"moo", "lion":"roar", "duck":"quack", "dog":"bork"}
##for things in dicty:
##    print(things, dicty[things])


##dicty = {1:"a",2:"b",3:"c",4:"d"}
##for things in dicty:
##    print(dicty[things] + str(things))


##dicty = {"Annie":1, "John":2}
##for things in dicty:
##    print(things, dicty[things])
##    print(things, dicty[things])


##dicty = {1:"",2:"",3:"",4:""}
##for things in dicty:
##    dicty[things] = 3*things
##print(dicty)


##a = {}
##for things in range(1, 6, 1):
##    print("Give me a name.")
##    name = input()
##    print("Give me a YOB.")
##    yob = input()
##    a[name] = yob
##print(a)


##zoo = { "lion" : 3, "tiger" : 5, "bear" : 6 } 
##a = {"hello" : zoo}
##print(a["hello"]["bear"])


##characters = { "lion" : ["Simba", 5], "tiger" : ["Tigress", 2], "panda" : ["Po", 8] } 
##a = {"hello" : characters}
##print(a["hello"]["panda"][0])


##characters = { "lion" : ["Simba", 5], "tiger" : ["Tigress", 2], "panda" : ["Po", 8] } 
##a = {"hello" : characters}
##for things in characters:
##    print(things, a["hello"][things][0], a["hello"][things][1])


##characters = { "lion" : ["Simba", 5], "tiger" : ["Tigress", 2], "panda" : ["Po", 8] } 
##a = {"hello" : characters}
##for things in characters:
##    print("The", things, "is called", a["hello"][things][0], "and its age is", str(a["hello"][things][1]) + ".")


##characters = { "lion" : ["Simba", 5], "tiger" : ["Tigress", 2], "panda" : ["Po", 8] } 
##a = {"hello" : characters}
##for things in characters:
##    print(a["hello"][things][0], a["hello"][things][1])


##oofy = {"goo":4, "oop":6, "qqqq":20, "qwrosof": 15, "fejfejje": 500}
##aaa = 0
##ham = None
##for things in oofy:
##    if oofy[things] > aaa:
##        ham = things
##print(ham)


##oofy = {"goo":4, "oop":6, "qqqq":20, "qwrosof": 15, "fejfejje": 500, "woeo" : 500}
##aaa = 0
##ham = []
##for things in oofy:
##    if oofy[things] > aaa:
##        if len(ham) > 0:
##            ham.pop()
##        ham.append(things)
##    if oofy[things] == aaa:
##        ham.append(things)
##    aaa = oofy[things]
##print(ham)

































