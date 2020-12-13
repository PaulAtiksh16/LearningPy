import random
wordslist = ["like","diligent","elderly","education","tiresome","creator","explode","waves","vengeful","error","hanging","plausible","existence","measly","cluttered","snobbish","awful","visit","letter","hope","load","governor"]
word = random.choice(wordslist)
wordinalist = list(word)
lives = 6
cheatcode = ":o"
wordspace = []
print("Let's play hangman! You have 6 lives.")
for blanks in range(len(word)):
    wordspace.append("_")
print(wordspace)
while True:
## Guessing
    print("Guess a letter!")
    guess = input()
## Cheatcode
    if guess == cheatcode:
        print("You have used the cheat code! I will reveal 1 letter.")
        while True:
            cheatberg = random.choice(wordinalist)
            if cheatberg not in wordspace:
                for wooboperot in range(len(wordinalist)):
                    if cheatberg in wordinalist[wooboperot]:
                        wordspace[wooboperot] = wordinalist[wooboperot]
                        if wordinalist == wordspace:
                            break
                print("You now have ",lives," lives.")
                break
## Normal guessing
    else:
        for wobo in range(len(wordinalist)):
            if guess == wordinalist[wobo]:
                wordspace[wobo] = guess
    print(wordspace)
## Lives
    if guess != cheatcode:    
        if guess not in wordinalist:
            lives = lives - 1
            print("You now have ",lives," lives.")
## Losing
        if lives == 0:
            print("You lose! All your lives are gone.")
            break
## Winning        
    if wordinalist == wordspace:
        print("You win! Your word was ",word,".")
        break
