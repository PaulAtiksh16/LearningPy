# class shapes:
#     def __init__(self, sides, name):
#         self.sides = sides
#         self.name = name
# rectangle = shapes(4, "rectangle")
# triangle = shapes(3, "triangle")
# circle = shapes(0, "circle")
# pentagon = shapes(5, "pentagon")
# print(rectangle.sides, rectangle.name)
# print(triangle.sides, triangle.name)
# print(circle.sides, circle.name)
# print(pentagon.sides, pentagon.name)


# class dog:
#     def __init__(self, name, eye_color, fur_color, breed, age):
#         self.name = name
#         self.eye_color = eye_color
#         self.fur_color = fur_color
#         self.breed = breed
#         self.age = age
#     def show_info(self):
#         print("My dog's name is", self.name, ", and he/she is a", self.age, "year old", self.breed, ", with", self.eye_color, "eyes and", self.fur_color, "colored fur.")
# doge = dog("Doge", "brown", "gold", "Shiba Inu", 3)
# doge.show_info()
# robot = dog("Robodoge", "blue", "silver", "robot", 1)
# robot.show_info()
# class person:
#     def __init__(self, name, gender, age, petlist):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.petlist = petlist
#     def pets(self):
#         for things in range(0, len(self.petlist), 1):
#             print(self.petlist[things])
#     def another(self):
#         print("Do you have another dog?")
#         another = input()
#         if another == "yes":
#             print("What's its name?")
#             newdog = input()
#             self.petlist.append(newdog)
# sam = person("Sam", "male", "16", [str(robot), str(doge)])
# sam.pets()


# class state:
#     def __init__(self, name, capital_city, population):
#         self.name = name
#         self.capital_city = capital_city
#         self.population = population
#     def capitol(self):
#         print(self.capital_city)
# california = state("California", "Sacramento", "39M")
# washington = state("Washington", "Olympia", "7M")
# new_york = state("New York", "Albany", "19M")
# arizona = state("Arizona", "Phoenix", "7M")
# texas = state("Texas", "Austin", "28M")
# states = [california, washington, new_york, arizona, texas]
# print("Which state do you want to research?")
# answer = input()
# for things in states:
#     if answer == things.name:
#         print(things.population)
#         print(things.capital_city)


# class shopping:
#     def __init__(self, name, cart):
#         self.name = name
#         self.cart = cart
#     def transaction(self):
#         print("What would you like to do? (Add/Remove)")
#         action = input()
#         if action == "add":
#             print("What is your item?")
#             item = input()
#             print("What is the quantity?")
#             quantity = int(input())
#             self.cart[item] = quantity
#         else:
#             print("What would you like to remove?")
#             gone = input()
#             self.cart.pop(gone)
#         print(self.cart)
# safeway = shopping("safeway", {"chocolate":2, "sugar":3, "milk":1, "yogurt":5, "salt":8})
# safeway.transaction()


# class phonebook:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#     def edit(self):
#         print("What would you like to do? (Add/Remove)")
#         action = input()
#         if action == "add":
#             print("What is your name?")
#             name = input()
#             print("What is the number?")
#             number = int(input())
#             self.phone[name] = number
#         else:
#             print("What would you like to remove?")
#             gone = input()
#             print("Are you sure you want to remove this?")
#             confirm = input()
#             if confirm == "yes":
#                 self.phone.pop(gone)
#         print(self.phone)
#     def check(self):
#         print("What is the name?")
#         phone_name = input()
#         if phone_name in self.phone:
#             print(self.phone[phone_name])
#         else:
#             print("Phone number not found")
# one = phonebook("one", {"mom":5105898778, "dad":5103642489, "shaan":9255480211})
# print("Would you like to edit or check?")
# response = input()
# if response == "edit":
#     one.edit()
# else:
#     one.check()


class zoo:
    def __init__(self, name, population, food, habitat):
        self.name = name
        self.population = population
        self.food = food
        self.habitat = habitat
    def edit(self):
        print("Would you like to add or remove?")
        response = input()
        if response == "add":
            print("What would you like to add?")
            addition = input()
            if addition in self.population:
                self.population[addition] = self.population[addition] + 1
            else:
                self.population[addition] = 1
                print("What does it eat?")
                supply = input()
                self.food[addition] = supply
                print("Where does it live?")
                house = input()
                self.habitat[addition] = house
        else:
            print("What would you like to remove?")
            response = input()
            if response not in self.population:
                print("We don't have that.")
            else:
                if self.population[response] > 1:
                    self.population[response] = self.population[response] - 1
                else:
                    self.population.pop(response)
                    self.food.pop(response)
                    self.habitat.pop(response)
        print(self.population)
        print(self.food)
        print(self.habitat)
    def info(self):
        print("Which animal would you like to see?")
        kreetur = input()
        if kreetur in self.population:
            print("There are", self.population[kreetur], kreetur + "s who live in a predominantly", self.habitat[kreetur], "location that eat", self.food[kreetur] + ".")
        else:
            print("We don't have that animal.")
sfo = zoo("sfo", {"lion":2, "toucan":5, "tiger":3}, {"lion":"meat", "toucan":"fruit", "tiger":"fruit"}, {"lion":"land", "toucan":"air", "tiger":"land"})
tokyo = zoo("tokyo", {"elephant":4, "rhino":3, "ostrich":10}, {"elephant":"plants", "rhino":"plants", "ostrich":"fruits and bugs"}, {"elephant":"land", "rhino":"land", "ostrich":"land"})
print("Which zoo?")
place = input()
if place == "sfo":
    print("Would you like info or to edit?")
    choice = input()
    if choice == "info":
        sfo.info()
    else:
        sfo.edit()
else:
    print("Would you like info or to edit?")
    choice = input()
    if choice == "info":
        tokyo.info()
    else:
        tokyo.edit()