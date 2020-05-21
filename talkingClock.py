"""
Sam Minix
5/21/20

https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
Description:
No more hiding from your alarm clock! You've decided you want your computer to keep you updated on
the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.

Input Description:
An hour (0-23) followed by a colon followed by the minute (0-59).

Output Description:
The time in words, using 12-hour format followed by am or pm.
"""
#dictionary of words
hourWord = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
tensWord = ["oh", "ten", "twenty", "thirty", "forty", "fifty", "sixty"] #the ten term functions more like a placeholder in this list
funkyTens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
onesWord = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def talkingClock(time):
    
    seperated = time.split(':') #seperate input to get hour and minutes
    hour = int(seperated[0])
    minute = int(seperated[1])
    
    if hour < 12: #determine morning or night
        light = "a.m." 
    else:
        light = "p.m."
    
    if minute // 10 == 0 and minute % 10 == 0: #if there is no minute, it is just the hour am/pm
        return("It's %s %s" %(hourWord[hour%12], light))

    if minute // 10 == 1: #time from 11 to 19 are funky, so made special list for them
        return("It's %s %s %s" %(hourWord[hour%12], funkyTens[minute % 10], light))

    else: #if not a funky time, include tens and ones place
        return("It's %s %s %s %s" %(hourWord[hour%12], tensWord[minute // 10], onesWord[minute % 10], light))



time = input("Enter the time in 24 hr format: ")
print(talkingClock(time))
