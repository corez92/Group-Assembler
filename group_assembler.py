import random

participants = []

group_size = 3
overflow = 'n'
# Check to see if possible to make well-balanced groups

while overflow == 'n':
    if len(participants) % int(group_size) != 0:
            overflow = input("There are {} participants over, do you want to add them to another group? Yes = y, No = n:\n".format(str(len(participants) % int(group_size))))
            if overflow == "y":
                break
            group_size = input("How big should the new groups be?".format(str(len(participants) % int(group_size))))
    else:
        overflow = 'resolved in while loop'
#group =
##groups = [participants[j] for i in range(len(participants) // int(group_size) + 1) for j in range(group_size)]
##
##group = []
##choices = [m for m in range(len(participants))]
##for i in range(len(participants) // int(group_size) + 1):
##    group = []
##    for j in range(group_size):
##        print("Before pop")
##        print(choices)
##        current_choice = choices.pop(random.choice(choices))
##        group.append(participants[current_choice])
##        print(current_choice)
##        print("After pop")
##        print(choices)
##        #print(choices)

random.shuffle(participants)
group1 = random.sample(participants,  group_size)
groups = [random.sample(participants,  group_size) for h in range(len(participants) // int(group_size) + 1)]
groups[random.choice(len(groups))].append
        
