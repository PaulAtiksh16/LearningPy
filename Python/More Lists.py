##numlist = []
##for num in range(1,1001,1):
##    if num%5 == 0 and num%15 != 0:
##        numlist.append(num)
##print(numlist)



##import random
##hobby = ["painting", "coin collection", "diving", "scuba diving"]
##profession = ["engineer", "doctor", "archaeologist", "swordsman"]
##age = [20,30,40,50]
##hobbychoice = random.choice(hobby)
##professionchoice = random.choice(profession)
##agechoice = random.choice(age)
##print("John is a(n)",professionchoice,"by profession. His favourite hobby is",hobbychoice,". He is",agechoice,"years


##listlist = []
##DantdmList = ["Dan","Asher","Jemma","Ellie","Darcie","Minecraft","Grim","Skinny","Diamond","Gaming"]
##for item in range(len(DantdmList)):
##    listlist.append(len(DantdmList[item]))
##print(listlist)


DantdmList = ["Dan","Asher","Jemma","Ellie","Darcie","Minecraft","Grim","Skinny","Diamond","Gaming"]
print("What letter do you want me to look for?")
letter = input()
for item in range(len(DantdmList)):
    if letter in DantdmList[item]:
        for letterbug in range(len(DantdmList[item])):
            if letter == DantdmList[item][letterbug]:
                print(DantdmList[item],letterbug+1)





                
