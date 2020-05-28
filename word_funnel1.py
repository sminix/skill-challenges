'''
Sam Minix
5/28/2020
https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/
Given two strings of letters, determine whether the second can be made from the first by removing one letter.
The remaining letters must stay in the same order.
'''
def word_funnel1 (str1, str2):
    
    if len(str2) > len(str1): #failure check, if str2 is longer is will always fail
        return False
    
    for i in range(len(str1)): #for every letter in str1

        new_str1 = str1[0:i] + str1[i+1:] #make a new string removing one letter at a time
        if new_str1 == str2: #if they are equal it is true
            return True

    return False #if after going though all the letter it isn't true, return false
'''
#Test Case
print(word_funnel1("leave", "eave")) #True
print(word_funnel1("reset", "rest")) #True
print(word_funnel1("dragoon", "dragon"))#True
print(word_funnel1("eave", "leave")) #False
print(word_funnel1("sleet", "lets")) #False
print(word_funnel1("skiff", "ski")) #False
'''

'''
Given a string, find all words from the enable1 word list that can be made by removing one letter from the string.
If there are two possible letters you can remove to make the same word, only count it once. Ordering of the output words doesn't matter.
'''
def bonus(word):
    reader = open("enable1.txt", "r") #open the enable1 list, this part is different depending on where it is stored
    funnel = [] #initiate list of funnel words
    for line in reader:
        if word_funnel1(word, line.strip()): #for each line compare the given word with the line
            funnel.append(line.strip()) #if it works, add it to the funnel list
    return funnel
'''
Test Cases
print(bonus("dragoon")) #['dragon']
print(bonus("boats")) #['bats', 'boas', 'boat', 'bots', 'oats']
print(bonus("affidavit")) #[]
'''

'''
Given an input word from enable1, the largest number of words that can be returned from bonus(word) is 5
One such input is "boats". There are 28 such inputs in total. Find them all.

In theory this code works but I can't figure out how to make it quicker
'''
def bonus2():
    reader = open("enable1.txt" ,"r")
    words = []
    for line in reader:
        if len(bonus(line.strip())) == 5:
            words.append(line.strip())

print(bonus2())
