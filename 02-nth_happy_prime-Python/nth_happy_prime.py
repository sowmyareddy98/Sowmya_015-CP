# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
	if (n < 2):
		return False
	if (n == 2):
		return True
	if (n % 2 == 0):
		return False
	maxFactor = round(n**0.5)
	for factor in range(3,maxFactor+1,2):
		if (n % factor == 0):
			return False
	return True
#helper function to find the squares of digits
def numSquareSum(n): 
	squareSum = 0; 
	while(n): 
		squareSum += (n % 10) * (n % 10); 
		n = int(n / 10); 
	return squareSum; 
  
#to find out if it is a happy number or not
def isHappynumber(n): 
  

	slow = n; 
	fast = n; 
	while(True): 
		  
	
   
		slow = numSquareSum(slow); 

		fast = numSquareSum(numSquareSum(fast)); 
		if(slow != fast): 
			continue; 
		else: 
			break; 
  

	return (slow == 1); 
#finding nth happy primes
def fun_nth_happy_prime(n):
	#return 0
	found = 0
	guess = 0
	while (found <= n):
		guess += 1
		#print(guess)
		if ((isHappynumber(guess)) and (isPrime(guess))):
			found += 1
			#print(guess)
	return guess