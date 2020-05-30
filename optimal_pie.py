'''
Sam Minix
Write an algorithm that determines the maximum number of pies that can be made
https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/
'''
PUMPKIN = [1, 3, 4, 3] #recipe totals, [0] is apple or pumpkin, [1] is eggs
APPLE = [1, 4, 3, 2] #[2] is milk and [3] is sugar
def pies(ingredients):
    ingredients = ingredients.split(',') #split the input into ingredieents
    pumpkins = int(ingredients[0])
    apples = int(ingredients[1])
    eggs = int(ingredients[2])
    milk = int(ingredients[3])
    sugar = int(ingredients[4])

    pies = [0, 0] #start with no pies
    for n in range(pumpkins): #n represents number of pumpkin pies
        nEggs = eggs - PUMPKIN[1]*n #calculate remaining ingredients for apple pies
        nMilk = milk - PUMPKIN[2]*n
        nSugar = sugar - PUMPKIN[3]*n
        if nEggs < 0 or nMilk < 0 or nSugar < 0: #if any ingredient is negative, break
            break
        limit = 100 #initialize limiting factor as high number

        if apples//APPLE[0] < limit: #These if statements determine the limiting factor in making apple pies
            limit = apples//APPLE[0] #limit ends up being max apple pies that can be made for n pumpkin

        if nEggs // APPLE[1] < limit:
            limit = nEggs // APPLE[1]

        if nMilk // APPLE[2] < limit:
            limit = nMilk// APPLE[2]

        if nSugar // APPLE[3] < limit:
            limit = nSugar // APPLE[3]
        
        if limit + n > sum(pies):  #if more pies can be made, update pie list
            pies = [n, limit]
            
    return("%d pumpkin pies and %d apple pies" %(pies[0], pies[1]))
#Test Cases
print(pies("10,14,10,42,24"))
print(pies("12,4,40,30,40"))
print(pies("12,14,20,42,24"))


        
    
    
