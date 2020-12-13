##print("Give me a string!!!")
##string = input()
##listberg = list(string)
##for var in range(len(listberg)):
##    print(listberg[var])


##print("Give me a sentence!!!")
##sentence = input()
##listbergerqueen = sentence.split()
##for var in listbergerqueen:
##    print(var)


import random
wordslist = ["like","diligent","elderly","education","tiresome","creator","explode","waves","vengeful","error","hanging","plausible","existence","measly","cluttered","snobbish","awful","visit","letter","hope","load","governor"]
word = random.choice(wordslist)
wordinalist = list(word)
lives = 6
cheatcode = ":o"
attempts = 0
wordspace = []
guesslist = []
print("Let's play hangman! You have 6 lives. There is a cheat code that will do something, but you can only use it if you do it before everything.")
for blanks in range(len(word)):
    wordspace.append("_ ")
print(wordspace)
print(word)
while True:
    print("Guess a letter!")
    guess = input()
    if guess == cheatcode:
        print("You have used the secret code! I will reveal one letter for you, but it will cost a life.")
        attempts = attempts + 1
        wordspace[0] = wordinalist[0]
    for wobo in range(len(wordinalist)):
        if guess == wordinalist[wobo]:
            wordspace[wobo] = guess
            guesslist.append(guess)
            attempts = attempts + 1
    print(wordspace)
    if guess not in wordinalist:
        lives = lives - 1
        print("You now have ",lives," lives.")
    if lives == 0:
        print("You lose! All your lives are gone.")
        break
    if attempts == len(word):
        print("You win! Your word was ",word,".")
        break



























        
