##import random
##words_list = ["quarantine", "television", "books", "movies", "comics"]
##raionnjd = random.choice(words_list)
##random_word = list(raionnjd)
##random.shuffle(random_word)
##while True:
##    print(random_word)
##    print("Guess what word this is!")
##    guess = input()
##    if guess == raionnjd:
##        print("You win! Your word was",raionnjd,"!")
##        break
##    else:
##        print("That was not your word. Try again!")



print("GIVE ME A WORD THIS INSTANT!!!")
word = input()
lists = []
for letters in range(len(word)):
    lists.append("*")
print(lists)
