# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	if (eggs<=0):
	 	return 0
	elif(eggs>0 and eggs<=12):
		return 1
	elif(eggs>12 and eggs<=24):
		return 2
	elif(eggs>24 and eggs<=36):
		return 3
