from utils import module_inverse


def findMinX(num, rem, k):
	'''
	Find the Chinese Remainder Theorem solution for the given number, and remainder.

	remainder = X % num

	parameters:
		num: the number to be divided (modulo)
		rem: the remainder to be found 
	returns:
		X: the solution to the given remainder and number
	'''
	
	# Compute product of all numbers
	prod = 1
	for i in range(0, k) :
		prod = prod * num[i]

	# Initialize result
	result = 0

	# Apply above formula
	for i in range(0,k):
		pp = prod // num[i]
		result = result + rem[i] * module_inverse(pp, num[i]) * pp
	
	
	return result % prod

# Driver method
# num = [3, 4, 5]

rem = [20,25]
num = [37,41]

# rem = [2, 3, 1]
k = len(num)
print( "x is " , findMinX(num, rem, k))

# This code is contributed by Nikita Tiwari.
