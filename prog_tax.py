'''
Create an algorithm to determine taxes owed in progressive taxation system
https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
'''
import math


#Code to gather tax rate information
caps = []
rates = []
while True:
    cap = input("Enter income cap, press enter for no cap: ")
    if cap == '':
        rate = input("Enter tax rate for above the cap: ")
        caps.append('--')
        rates.append(float(rate))
        break
        
    else:
        while True:
            rate = input("Enter tax rate for %s cap, in decimal form: " %(cap))
            if rate == '':
                continue
            else:
                caps.append(int(cap))
                rates.append(float(rate))
                break

def prog_tax(income):
    total = 0
    for i in range(len(caps) - 1): #for each tax cap

        if income < caps[i]:#if statements determine how total is add for this cap
            break
        
        if caps[i + 1] == '--': 
            total += (income - caps[i]) * rates[i + 1]
            break
        
        if income < caps[i + 1]:
            total += (income - caps[i]) * rates[i + 1]

        else:
            total += (caps[i + 1] - caps[i]) * rates[i + 1]

    return math.floor(total)
#Test Cases           
print(prog_tax(0))  #0
print(prog_tax(10000)) #0
print(prog_tax(10009)) #0
print(prog_tax(10010)) #1
print(prog_tax(12000)) #200
print(prog_tax(56789)) #8697
print(prog_tax(1234567)) #473326
    
    
