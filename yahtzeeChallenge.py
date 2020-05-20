"""
Sam Minix
May 20, 2020
https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results in a number of ways.
You are given a Yahtzee dice roll, represented as a sorted list of 5 integers, each of which is between
1 and 6 inclusive. Your task is to find the maximum possible score for this roll in the upper section of
the Yahtzee score card.
"""
import time
def yahtzee(roll):
    #find amount of dice rolls
    length = len(roll) 
    #initialize lists for storing values and counting
    values = []
    count = []
    """
    for loop that iterates through list of dice, for each unique die value add it to
    values list and increment same index for count
    """
    for i in range(length):
        #if roll value not in value list
        if roll[i] not in values:
            #append it and append 1 to count list
            values.append(roll[i])
            count.append(1)
            
        else:
            #if dice value already recorded, find index of value in values
            index = values.index(roll[i])
            #increment same count index
            count[index] = count[index] + 1

    """
    this for loop takes the value and multiplies it by it associated count
    """
    for i in range(len(values)):
        values[i] = values[i] * count[i]

    return max(values)

"""
This chunk allows the user to input the dice rolls, one die at a time
"""
roll = []
x = True
while x:
    dice = input("Enter dice value, press enter to stop: ")
    if dice == "":
        x = False

    else:
        roll.append(int(dice))

start_time = time.time()
print(yahtzee(roll))
end_time = time.time()
print(str(round(end_time - start_time, 5)) + " seconds") #see the runtime
