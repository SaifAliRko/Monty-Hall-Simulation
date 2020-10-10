import random

# Now we create a functionc modelling a player that always switches doors when he has been given option

def switching_player():

    doors = [1,2,3]
    car_behind_door = random.choice(doors)
    player_first_choice = random.choice(doors)

    if car_behind_door != player_first_choice :

        eliminate_door = [1,2,3]

        eliminate_door.remove(car_behind_door) # the door is removed by back of which is a car
        eliminate_door.remove(player_first_choice) # as he is switching so removing his door as well

        #now eliminate_door is left with one door where goat is ....ie which will be offered to the player_first_choice

        doors.remove(eliminate_door[0])
        doors.remove(player_first_choice)

        # now we assume that he switches and goes to the third door behind which might be car
        player_second_choice = doors[0]

        #now we will see if he wins or not

        if player_second_choice == car_behind_door:
            return 1

        else:
            return 0

    else:

        eliminate_door =[1,2,3]
        eliminate_door.remove(player_first_choice)
        eliminate_door = random.choice(eliminate_door)
        doors.remove(eliminate_door)
        doors.remove(player_first_choice)
        player_second_choice = doors[0]

        if player_second_choice == car_behind_door :
            return 1
        else:
            return 0

# Now for the player that does not switches

def non_switching_player():

    doors = [1,2,3]
    car_behind_door = random.choice(doors)
    player_first_choice = random.choice(doors)

    if player_first_choice == car_behind_door :
        return 1
    else:
        return 0

# Now to check our simulation and get results ie which thing is better to do switching or non switching

trials = 10000
number_of_trials = trials
switching_result = 0
non_switching_result = 0

while number_of_trials > 0 :

    switching_result = switching_result + switching_player()  # as the result of switching_player can be 1 or 0 so you wil get end results
    non_switching_result = non_switching_result + non_switching_player()  # same where
    number_of_trials = number_of_trials -1

print(f"By switching , out of {number_of_trials} attempts , i won {switching_result}times")
print(f"By switching , out of {number_of_trials} attempts , i won {non_switching_result}times")
