##nums = {1:"",2:"",3:"",4:"",5:""}
##for num in nums:
##    nums[num] =  num*num
##print(nums)


##dictberg = {}
##print("Give me a string!")
##string = input()
##for letter in range(len(string)):
##    dictberg[string[letter]] = letter
##print(dictberg)


##days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
##activities = ["Nothing","Drumline","Mathcounts","Coding","Drums","Karate","Math"]
##daily_activities = {}
##for monsters in range(len(days)):
##    daily_activities[days[monsters]] = activities[monsters]
##print(daily_activities)


##animals = {"dog":"","cat":"","elephant":"","duck":"","lion":""}
##for things in animals:
##    print("What sound does a",things,"make?")
##    sound = input()
##    animals[things] = sound
##print(animals)


fail_list = []
student_scores = {"Garfield":95,"Odie":43,"Jon":45}
for things in student_scores:
    student_scores[things] = student_scores[things] + 5
    if student_scores[things] >= 99:
        student_scores[things] = "A+"
    elif 89 <= student_scores[things] < 99:
        student_scores[things] = "A"
    elif 79 <= student_scores[things] < 89:
        student_scores[things] = "B"
    elif 69 <= student_scores[things] < 79:
        student_scores[things] = "C"
    elif 49 <= student_scores[things] < 69:
        student_scores[things] = "D"
    elif student_scores[things] <= 49:
        student_scores[things] = "F"
    if student_scores[things] == "F":
        fail_list.append(things)
print(student_scores)
for stuff in range(len(fail_list)):
    del(student_scores[fail_list[stuff]])
print(student_scores)
