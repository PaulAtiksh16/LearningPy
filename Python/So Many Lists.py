##poplist = []
##listberg = ["mask","gloves","quarantine","virus","distance","shelter","online","inside","interaction","zoom"]
##for hamsters in range(len(listberg)):
##    if hamsters%2 != 0:
##        poplist.append(listberg[hamsters - 1])
##print(poplist)



import random
mylist = []
otherlist = []
for num in range(1,11,1):
    mylist.append(random.randint(1,200))
for gooloogooloo in range(len(mylist)):
    if mylist[gooloogooloo]%5 == 0:
        otherlist.append(mylist[gooloogooloo])
print(mylist)
print(otherlist)
