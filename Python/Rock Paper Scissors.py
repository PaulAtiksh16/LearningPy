import random
stuff = ["rock","paper","scissors"]
while True:
    print("Do you want to play rock, paper, scissors?")
    play = input()
    if play == "yes":
        print("Choose rock, paper, or scissors!")
        choice = input()
        goo = random.choice(stuff)
        print(goo)
        if choice == goo:
            print("It's a tie!")
        elif choice == "rock" and goo == "scissors":
            print("You win!")
        elif choice == "paper" and goo == "rock":
            print("You win!")
        elif choice == "scissors" and goo == "paper":
            print("You win!")
        elif goo == "rock" and choice == "scissors":
            print("You lose")
        elif goo == "paper" and choice == "rock":
            print("You lose")
        elif goo == "scissors" and choice == "paper":
            print("You lose")
    else:
        break
