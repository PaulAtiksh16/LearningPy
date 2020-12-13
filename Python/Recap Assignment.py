###setup
##while True:
##    print("Do you want to play a game?")
##    goomba = input()
##    if goomba == "yes":
##        import random
##        print("What game do you want to play? (coin toss or number guessing game)")
##        game = input()
##
##        #coin toss
##        if game == "coin toss":
##            choices = ["heads","tails"]
##            coin_guesslist = []
##            coin_score = 0
##            coin_computerlist = []
##            for things in range(1,11,1):
##                print("Choose a side. (heads or tails)")
##                side = input()
##                coin_guesslist.append(side)
##                ai = random.choice(choices)
##                coin_computerlist.append(ai)
##                if side == ai:
##                    print("You got a match!")
##                    coin_score = coin_score + 1
##                else:
##                    print("You got it wrong.")
##            print("You got",coin_score,"right out of 10!")
##            print()
##            print("This is what you guessed:",coin_guesslist)
##            print()
##            print("This is what the computer picked:",coin_computerlist)
##
##        #number guessing game
##        elif game == "number guessing game":
##            number_guesslist = []
##            number = random.randint(1,10)
##            while True:
##                print("Guess a number between one and ten!")
##                guess = int(input())
##                number_guesslist.append(guess)
##                if number == guess:
##                    print("You got it! Your number was",number)
##                    print()
##                    print("You guessed",number_guesslist)
##                    break
##                if guess > number:
##                    print("The number that was chosen is lower than that.")
##                if guess < number:
##                    print("The number that was chosen is higher than that.")
##
##        #other game
##        else:
##            print("Sorry, we don't have that game.")
##    else:
##        break



##print("Give me a number")
##one = int(input())
##print("Give me another")
##two = int(input())
##print("What operation do you want me to do? (addition, subtraction, multiplication, division)")
##operation = input()
##if operation == "addition":
##    print(one + two)
##elif operation == "subtraction":
##    print(one - two)
##elif operation == "multiplication":
##    print(one * two)
##else:
##    print(one / two)


##print("Do you like chocolate?")
##chocolate = input()
##if chocolate == "yes":
##    print("Do you like peanut butter?")
##    peanuts = input()
##    if peanuts == "yes":
##        print("Try a Reese's Cup.")
##    else:
##        print("Try a Hershey's Bar.")
##else:
##    print("There's something wrong with you. Goodbye.")


##print("Give me a number.")
##number = int(input())
##if number == 4:
##    print("Mmmmmmmmmmmm... DELICIOUS!!!")
##elif number > 0 and number != 4:
##    print("That's okay... Thanks.")
##else:
##    print("DISGUSTING! Why would you give me this?!")


##oof = 0
##while True:
##    print("Do you want to count?")
##    count = input()
##    if count == "no" and oof == 0:
##        print("Thanks, meanie.")
##        break
##    if count != "no":
##        for number in range(1,11,1):
##            print(number)
##            oof = oof + 1
##    if count == "no" and oof > 0:
##        print("Thanks for learning to count with me!")
##        break
            

##numbers = [4,8,12,16,20,24,28,32,36,40]
##words = ["cat","dog","sheep","frog","tiger","lion","bird","dagger","giraffe","zebra"]
##print(words[6])
##words[3] = 72
##numbers[1] = numbers[1] + 1
##words.append("monsters")
##words.insert(7,"fish")
##words.remove("dog")
##numbers.pop(4)
##for things in range(len(words)):
##    print(words[things])
##for thingbergs in range(len(numbers)):
##    print(numbers[thingbergs])


##namelist = []
##numberlist = []
##dictionary = {"Shaan":94517,"Gabardo":76539,"Opratina":43786,"Yulang":12038,"Raqued":36124}
##dictionary["Doggo"] = 76134
##dictionary["Gabardo"] = 34582
##dictionary["Opratina"] = dictionary["Opratina"] + 800000
##dictionary.pop("Yulang")
##for things in dictionary:
##    print(things)
##    namelist.append(things)
##for things in dictionary:
##    print(dictionary[things])
##    numberlist.append(dictionary[things])
##for things in dictionary:
##    print(things, dictionary[things])
##    print(dictionary[things],things)
##numberlist.sort()
##for thingamajigs in range(len(numberlist)):
##    for thingamabobs in dictionary:
##        if numberlist[thingamajigs] == dictionary[thingamabobs]:
##            print(thingamabobs,numberlist[thingamajigs])
