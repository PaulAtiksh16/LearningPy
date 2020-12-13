##pres = open("presidents.txt",'r')
##f=pres.read()
##print(f)
##f=pres.readline()
##print(f)
##for lines in pres:
##        print(lines)
##pres.close()
##with open("presidents.txt",'r') as pres: 
##     f = pres.read()
##     print(f)
##with open("presidents.txt",'r') as pres: 
##    f = pres.readline()
##    print(f)
##with open("presidents.txt",'r') as pres: 
##    for lines in pres:
##        print(lines)


##pres = open("presidents.txt",'w')
##pres.write("Barack Obama")        
##pres.close()
##pres = open("presidents.txt",'a')
##pres.write(" Donald Trump")        
##pres.close()
##pres = open("presidents.txt","r")
##for lines in pres:
##        print(lines)
##pres.close()


##line = 1
##import time
##test = open("test_file.txt","r")
####f = test.read()
####print(f)
##for lines in test:
##    print(line,lines)
##    time.sleep(1)
##    line = line + 1


##import random
##total = 0
##num = open("thousand.txt", "w")
##for things in range(1, 1001, 1):
##    randomint = (random.randint(1,1001))
##    num.write((str(randomint)) + "\n")
##    total = total + randomint
##num.close()
##numberg = open("thousand.txt", "r")
##for lines in numberg:
##    print(lines)
##numberg.close()
##print(total)


##print("What file would you like to copy from?")
##file = input()
##blah = open(file + ".txt","r")
##momo = blah.read()
##blah.close()
##gulu = open("copy_file.txt","w")
##gulu.write(momo)
##gulu.close()
##gaba = open("copy_file.txt","r")
##for lines in gaba:
##    print(lines)
##gaba.close()


##words = 0
##blah = open("all_words.txt", "r")
##for lines in blah:
##    words = words + 1
##blah.close()
##if words > 0:
##    print(words)
##else:
##    print("No words found.")


##why = 0
##letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,}   
##blah = open("all_words.txt", "r")
##print("Give me a letter.")
##one = input()
##print("Give me another.")
##two = input()
##print("Give me another.")
##three = input()
##for lines in blah:
##    glob = lines
##    if "a" == glob[0]:
##        letters["a"] = letters["a"] + 1
##    if "b" == glob[0]:
##        letters["b"] = letters["b"] + 1
##    if "c" == glob[0]:
##        letters["c"] = letters["c"] + 1
##    if "d" == glob[0]:
##        letters["d"] = letters["d"] + 1
##    if "e" == glob[0]:
##        letters["e"] = letters["e"] + 1
##    if "f" == glob[0]:
##        letters["f"] = letters["f"] + 1
##    if "g" == glob[0]:
##        letters["g"] = letters["g"] + 1
##    if "h" == glob[0]:
##        letters["h"] = letters["h"] + 1
##    if "i" == glob[0]:
##        letters["i"] = letters["i"] + 1
##    if "j" == glob[0]:
##        letters["j"] = letters["j"] + 1
##    if "k" == glob[0]:
##        letters["k"] = letters["k"] + 1
##    if "l" == glob[0]:
##        letters["l"] = letters["l"] + 1
##    if "m" == glob[0]:
##        letters["m"] = letters["m"] + 1
##    if "n" == glob[0]:
##        letters["n"] = letters["n"] + 1
##    if "o" == glob[0]:
##        letters["o"] = letters["o"] + 1
##    if "p" == glob[0]:
##        letters["p"] = letters["p"] + 1
##    if "q" == glob[0]:
##        letters["q"] = letters["q"] + 1
##    if "r" == glob[0]:
##        letters["r"] = letters["r"] + 1
##    if "s" == glob[0]:
##        letters["s"] = letters["s"] + 1
##    if "t" == glob[0]:
##        letters["t"] = letters["t"] + 1
##    if "u" == glob[0]:
##        letters["u"] = letters["u"] + 1
##    if "v" == glob[0]:
##        letters["v"] = letters["v"] + 1
##    if "w" == glob[0]:
##        letters["w"] = letters["w"] + 1
##    if "x" == glob[0]:
##        letters["x"] = letters["x"] + 1
##    if "y" == glob[0]:
##        letters["y"] = letters["y"] + 1
##    if "z" == glob[0]:
##        letters["z"] = letters["z"] + 1
##
##    if (one in glob) and (two in glob) and (three in glob):
##        print(glob)
##
##    if "y" == glob[-2]:
##        why = why + 1
##
##    gulu = glob.strip()
##    if gulu == gulu[::-1]:
##        print(gulu)
##
##print(letters)
##print(why)


# import os
# print("Give me a file name.")
# fileberg = input()
# exists = os.path.isfile(fileberg)
# if exists:
#   print("File found")
# else:
#   print("File not found")


# golo = open("good.txt","r")
# dudu = golo.readlines()
# dede = open("good.txt","w")
# for things in dudu:
#   dede.write(things.replace(" ","_"))
# for lines in dudu:
#   print(lines)
# golo.close()
# dede.close()


score = 0
print("What's your name?")
name = input()

you = open(name + ".txt","w")

blogh = open("questions.txt","r")
juju = blogh.readlines()

falop = open("answers.txt","r")
vaca = falop.readlines()

for lines in range(0,10,1):
  print(juju[lines])
  oof = input()
  you.write(oof + "\n")
  if oof == (vaca[lines]).strip():
    print("Correct")
    score = score + 1
  else:
    print("Incorrect")

blogh.close()
you.close()

mana = open(name + ".txt", "r")
ham = mana.readlines()

for lineberg in range(0,10,1):
    print((ham[lineberg]).strip(),(vaca[lineberg]).strip())
    print()
print("You got",score,"out of 10!")

falop.close()
mana.close()


















