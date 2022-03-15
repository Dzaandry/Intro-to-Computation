def getBinaryRep(n, numDigits):
	"""Assumes n and numDigits are non-negative ints
	   Returns a str of length numDigits that is 
	   a binary representation of n"""
	result = ''
	while n > 0:
		result = str(n%2) + result
		n = n//2
	if len(result) > numDigits:
		raise ValueError('not enough digits')
	for i in range(numDigits - len(result)):
		result = '0' + result
	return result

def genPowerSet(L):
	"""Assumes L is a list
	   Returns a list of lists that contains all possible
	   combinations of the elements of L. E.g., if L is [1,2]
	   it will return a list with elements [], [1], [2], [1,2]."""
	powerset = []
	for i in range(0, 2**len(L)):
		binStr = getBinaryRep(i, len(L))
		subset = []
		for j in range(0, len(L)):
			if binStr[j] == '1':
				subset.append(L[j])
		powerset.append(subset)
	return powerset

print(len(genPowerSet(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])))

#O(2^len(L)) complexity