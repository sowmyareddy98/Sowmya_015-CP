# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	#pass
	if a==[]:
		return -1
	diff=10**20
	n=len(a)
	for i in range(n-1):
		for j in range(i+1,n):
			if abs(a[i]-a[j]) < diff:
				diff = abs(a[i] -a[j])
	return diff