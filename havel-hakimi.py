"""
Sam Minix
5/21/20
https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/
"""

"""
--------
WARMUPS / HELPER METHODS
--------
"""
#given a list l, remove all zeroes from it
def elim_zero(l):
    new_l = []
    for num in l:
        if num != 0:
            new_l.append(num)
    return new_l
#test case
#print(elim_zero([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])) => [5,3,2,6,2,7,2,5]
            
#given list l, sort in descending order (large -> small)
#implementation of merge sort with help from https://www.geeksforgeeks.org/merge-sort/
def descend_sort(l):
    length = len(l)
    #if the length is greater than 1, it can be sorted
    if length > 1:
        mid = length // 2 #find the midpoint to divide the 2 sides
        L = l[:mid]
        R = l[mid:]

        descend_sort(L) #recursive call for both sides
        descend_sort(R)

        i = j = k = 0 #initialize index variables

        while i < len(L) and j < len(R): #while the index variables are within right and left side
            if L[i] > R[j]: #if the left side is larger, replace l index with L
                l[k] = L[i]
                i += 1
            else:           #else, replace l index with R value
                l[k] = R[j]
                j += 1
            k += 1

        while i < len(L): #check if there are anymore in both lists
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1
            
    return l #return the list
#test
#print(descend_sort([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])) => [7,6,5,5,3,2,2,2,0,0,]

#Given a number N and a list l, return true if N is greater than the length of l
def length_check(N, l):
    return True if N > len(l) else False
#test
#print(length_check(7, [6, 5, 5, 3, 2, 2, 2]))

#Given an number N and a list l, subtract 1 from the first N elements
def front_elim(N, l):
    l[0:N] = [l[i] - 1 for i in range(N)]
    return l
#test
#print (front_elim(4, [5,4,3,2,1])) => [4,3,2,1,1]


"""
Havel-Hakimi Algorithm
Determine if a graph with the corresponding graph sequence can exist
"""
def havel_hakimi(l):
    l = elim_zero(l) #Remove all zeroes
    if len(l) == 0: #if the list is empty, graph is possible soreturn True
        return True

    
    l = descend_sort(l)#sort in descending order
    """
    After looking through some of the comments i see there is a sort function in
    Python, whcih would simplify/eliminate my helper method
    """
    N = l.pop(0) #Remove the first number and save it

    if length_check(N,l): #if N is larger than the length of the list
        return False #graph is not possible
    else:
        l = front_elim(N, l) #if not, subtract one from first N elements
        return havel_hakimi(l) #recursive call

"""
tests
print(havel_hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])) => false
print(havel_hakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16])) => true
print(havel_hakimi([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))=> false
print(havel_hakimi([])) => true
"""
