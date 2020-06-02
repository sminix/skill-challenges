'''
Sam Minix
6/2/20
Create a game like the Mastermind puzzle game or hacking minigame from falloout
https://www.reddit.com/r/dailyprogrammer/comments/3qjnil/20151028_challenge_238_intermediate_fallout/
'''
import random
#Find the possible words and answer to set up mastermind game
def setUp(difficulty):
    difficulty = int(difficulty)
    if difficulty == 1: #if Statements determine length of words and number of words
        length = random.choice([4,5])
        numWords = random.choice([5,6])
    elif difficulty == 2:
        length = random.choice([6,7])
        numWords = random.choice([7,8])
    elif difficulty == 3:
        length = random.choice([8,9,10])
        numWords = random.choice([9,10,11])
    elif difficulty == 4:
        length = random.choice([11,12,13])
        numWords = random.choice([12,13])
    elif difficulty == 5:
        length = random.choice([14,15])
        numWords = random.choice([14,15])
    else: 
        difficulty = input("Select a difficulty between 1 and 5: ") #failed to enter proper input
        masterMind(difficulty)

    reader = open("enable1.txt", "r") #read list of words
    possibleWords = []
    for line in reader:
        if len(line.strip()) == length: #if a word is appropriate length
            possibleWords.append(line.strip()) #add it to list of possible words

    qWords = [] 
    for i in range(numWords): #for the amount of question words, randomly select from possible words
        qWords.append(random.choice(possibleWords))

    answer = random.choice(qWords) #randomly choose answer from question words

    masterMind(answer, qWords)

#handles asking for guesses from player
def masterMind(answer, words):
    
    for i in range(len(words)): #print words
        print(words[i])
        
    win = False 
    for i in range(4): #4 guesses
        guess = input("Guess #%d? " %(i + 1))
        count = checker(guess, answer) #check guess
        print("%d/%d Correct" %(count, len(answer))) 
        if count == len(answer): #if right
            print("You Win!")
            win = True
            break
        
    if win == False:
        print("You Lose!")

#checks the guesses and returns the amount of letters correct
def checker(guess, answer):
    count = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]: #count number of right letters
            count += 1

    return count
    

    

setUp(input("Difficulty (1-5)? "))
    
    
    
    
