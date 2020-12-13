##for things in range(33,257,1):
##    print(chr(things))


##print("What is your name?")
##name = input()
##print("How old are you?")
##age = input()
##print("What state do you live in?")
##state = input()
##print("My name is {0}. I am {1} year(s) old. I live in {2}.".format(name, age, state))


##print("Give me some strings separated by commas.")
##strings = input()
##listberg = list(strings.split(","))
##for things in range(len(listberg)):
##    print(listberg[things])


##print("Give me some numbers separated by spaces.")
##strings = input()
##listberg = list(strings.split(" "))
##for things in range(len(listberg)):
##    if int(listberg[things])%2 == 0:
##        print(listberg[things])


print("Give me a string.")
string = input()
liststring = list(string)
liststring.reverse()
antistring = "".join(liststring)
if antistring == string:
    print("You have a palindrome!")
else:
    print("You don't have a palindrome.")
