from datetime import datetime
counter = 0
print("Let's play the mash game! Mash enter as many times as you can in ten seconds. Ready?")
print()
print("GO!")
time_now = datetime.now()
good_time = int(time_now.strftime("%S"))
while True:
    next_time = datetime.now()
    oof_time = int(next_time.strftime("%S"))
    print("")
    space = input()
    if space == "":
        counter = counter + 1
    if oof_time == good_time + 10:
        break
print("You pushed enter",counter,"times in ten seconds!")
        
