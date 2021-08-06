# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

import math
def checkPronic(x) :
    i = 0
    while ( i <= (int)(math.sqrt(x)) ) :
         
        # Checking Pronic Number
        # by multiplying consecutive
        # numbers
        if ( x == i * (i + 1)) :
            return True
        i = i + 1
 
    return False
 
def nthpronicnumber(n):
    count=0
    j=0
    while(count<=n):
        if(checkPronic(j)):
            count+=1
            res=j
        j+=1
    return res