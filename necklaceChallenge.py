"""
Sam Minix
5/20/20
From daily programmer challenge on reddit

(https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/)
Imagine a necklace with lettered beads that can slide along the string. Here's an example image. In this
example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN. Do it again
to get COLENI, and so on. For the purpose of today's challenge, we'll say that the strings "nicole", "icolen",
and "coleni" describe the same necklace. Generally, two strings describe the same necklace if you can remove
some number of letters from the beginning of one, attach them to the end in their original ordering, and get
the other string. Reordering the letters in some other way does not, in general, produce a string that describes
the same necklace.

Write a function that returns whether two strings describe the same necklace.
"""
def isNecklace(str1, str2):
    
    length = len(str1) #find length of the first string
    
    if length != len(str2): #check if the two strings are the same lengh
        return False
    
    if length == 0: #if both strings have equal length and the lenght is 0, it is true
        return True
    
    i = 0
    """
    for loop to manipulate first string
    """
    while i <= length:  
        char = str1[0] #save the first letter of the string
        str1 = str1[1:] #this removes the first letter
        str1 += char #adds the first letter back, but now to the end
        if str1 == str2:
            return True #if they are equal now, then it is true
        i += 1
    return False #If after all iterations the strings were not equal, stop
 

firstWord = input("Enter the first word: ")
secondWord = input("Enter the second word: ")
print(isNecklace(firstWord, secondWord))
          
        
