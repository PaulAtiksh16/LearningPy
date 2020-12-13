player = "player1"
print("Let's play tic tac toe!")
#Setup
toes = {1:": ",2:": ",3:": ",4:": ",5:": ",6:": ",7:": ",8:": ",9:": "}
for things in toes:
    if things <= 3:
        print(things,toes[things], end = " ")
print()
for things in toes:
    if 3 < things < 7:
        print(things,toes[things], end = " ")
print()
for things in toes:
    if things >= 7:
        print(things,toes[things], end = " ")
print()
#Game start
while True:
    end = "no"
#Player1 choice system
    if player == "player1":
        print("Player 1, pick a number 1 through 9.")
        choice = int(input())
        while True:
            if toes[choice] == ": ":
                toes[choice] = ":X"
                break
            else:
                print("Sorry, that spot's taken. Choose another one!")
                choice = int(input())
        for things in toes:
            if things <= 3:
                print(things,toes[things], end = " ")
        print()
        for things in toes:
            if 3 < things < 7:
                print(things,toes[things], end = " ")
        print()
        for things in toes:
            if things >= 7:
                print(things,toes[things], end = " ")
        print()
        player = "player2"
#Player1 win system
    if (toes[1] == ":X" and toes[2] == ":X" and toes[3] == ":X") or \
        (toes[4] == ":X" and toes[5] == ":X" and toes[6] == ":X") or \
        (toes[7] == ":X" and toes[8] == ":X" and toes[9] == ":X") or \
        (toes[1] == ":X" and toes[4] == ":X" and toes[7] == ":X") or \
        (toes[2] == ":X" and toes[5] == ":X" and toes[8] == ":X") or \
        (toes[3] == ":X" and toes[6] == ":X" and toes[9] == ":X") or \
        (toes[1] == ":X" and toes[5] == ":X" and toes[9] == ":X") or \
        (toes[3] == ":X" and toes[5] == ":X" and toes[7] == ":X"):
            print("Player 1 has won!")
            end = "yes"
#Draw system
    if (toes[1] != ": " and toes[2] != ": " and toes[3] != ": " and toes[4] != ": " and toes[5] != ": " and toes[6] != ": " and toes[7] != ": " and toes[8] != ": " and toes[9] != ": "):
        print("It's a draw!")
        end = "yes"
#Play again system
    if end == "yes":
        print("Do you want to play again?")
        answer = input()
        if answer == "yes":
            for weirdos in toes:
                toes[weirdos] = ": "
            toes = {1:": ",2:": ",3:": ",4:": ",5:": ",6:": ",7:": ",8:": ",9:": "}
            for things in toes:
                if things <= 3:
                    print(things,toes[things], end = " ")
            print()
            for things in toes:
                if 3 < things < 7:
                    print(things,toes[things], end = " ")
            print()
            for things in toes:
                if things >= 7:
                    print(things,toes[things], end = " ")
            print()
            player = "player1"
            end = "no"
        else:
            break
#Player2 choice system
    if player == "player2":
        print("Player 2, pick a number 1 through 9.")
        choice = int(input())
        while True:
            if toes[choice] == ": ":
                toes[choice] = ":O"
                break
            else:
                print("Sorry, that spot's taken. Choose another one!")
                choice = int(input())
        for things in toes:
            if things <= 3:
                print(things,toes[things], end = " ")
        print()
        for things in toes:
            if 3 < things < 7:
                print(things,toes[things], end = " ")
        print()
        for things in toes:
            if things >= 7:
                print(things,toes[things], end = " ")
        print()
        player = "player1"
#Player2 win system
    if (toes[1] == ":O" and toes[2] == ":O" and toes[3] == ":O") or \
        (toes[4] == ":O" and toes[5] == ":O" and toes[6] == ":O") or \
        (toes[7] == ":O" and toes[8] == ":O" and toes[9] == ":O") or \
        (toes[1] == ":O" and toes[4] == ":O" and toes[7] == ":O") or \
        (toes[2] == ":O" and toes[5] == ":O" and toes[8] == ":O") or \
        (toes[3] == ":O" and toes[6] == ":O" and toes[9] == ":O") or \
        (toes[1] == ":O" and toes[5] == ":O" and toes[9] == ":O") or \
        (toes[3] == ":O" and toes[5] == ":O" and toes[7] == ":O"):
            print("Player 2 has won!")
            end = "yes"
#Draw system
    if (toes[1] != ": " and toes[2] != ": " and toes[3] != ": " and toes[4] != ": " and toes[5] != ": " and toes[6] != ": " and toes[7] != ": " and toes[8] != ": " and toes[9] != ": "):
        print("It's a draw!")
        end = "yes"
#Play again system
    if end == "yes":
        print("Do you want to play again?")
        answer = input()
        if answer == "yes":
            for weirdos in toes:
                toes[weirdos] = ": "
            toes = {1:": ",2:": ",3:": ",4:": ",5:": ",6:": ",7:": ",8:": ",9:": "}
            for things in toes:
                if things <= 3:
                    print(things,toes[things], end = " ")
            print()
            for things in toes:
                if 3 < things < 7:
                    print(things,toes[things], end = " ")
            print()
            for things in toes:
                if things >= 7:
                    print(things,toes[things], end = " ")
            print()
            player = "player1"
            end = "no"
        else:
            break
