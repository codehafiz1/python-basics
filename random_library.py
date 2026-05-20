import random
number = random.randint(1,100)
print(number)
#For random number
list1 = ["Gaming","Coding","Studying","Reciting Holy Quran","Preparing for Exams","Talking with Friends"]
pick =random.choice(list1)
print(pick)
#For Random Choice from a List
list2 = list1
random.shuffle(list2)
print(f"Shuffled list {list2}")
#For Shuffling a List
