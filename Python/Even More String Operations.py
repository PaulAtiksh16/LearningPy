##january = "January"
##february = "February"
##march = "March"
##april = "April"
##may = "May"
##june = "June"
##july = "July"
##august = "August"
##september = "September"
##october = "October"
##november = "November"
##december = "December"
##months = january[0:3] + february[0:3] + march[0:3] + april[0:3] + june[0:3] + july[0:3] + august[0:3] + september[0:3] + october[0:3] + november[0:3] + december[0:3]
##print(months)
##one = months[0:3]
##two = months[3:6]
##three = months[6:9]
##four = months[9:12]
##five = months[12:15]
##six = months[15:18]
##seven = months[18:21]
##eight = months[21:24]
##nine = months[24:27]
##ten = months[27:30]
##eleven = months[30:33]
##twelve = months[33:36]
##print("Give me a number between one and twelve.")
##number = int(input())
##print(months[(number-1)*3:((number-1)*3)+3])


print("Give me a string.")
string = input()
for things in range(len(string)):
    print(ord(string[things]))
