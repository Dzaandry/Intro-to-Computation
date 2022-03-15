# complexity: O(len(L)^2)
def selectionSort(L):
	"""Assumes that L is a list of elements that can be compared using >.
	   Sorts L in ascending order."""
	suffixStart = 0
	while suffixStart < len(L):
		for i in range(suffixStart, len(L)):
			if L[i] < L[suffixStart]:
				L[suffixStart], L[i] = L[i], L[suffixStart]
		suffixStart += 1
	return L

# complexity: O(n*log(n)), where n is len(L).
def merge(left, right, compare):
	"""Assumes left and right are sorted lists and compare
	   defines an ordering on the elements.
	   Returns a new sorted (by compare) list containing 
	   the same elements as 
	   (left + right) would contain."""

	result = []
	i, j = 0, 0
	while (i < len(left)) and (j < len(right)):
		if compare(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	print('in merge. Result =', result)
	return result

def mergeSort(L, compare = lambda x, y: x < y):
	"""Assumes L is a list, compare defines an ordering
	   on elements of L.
	   Returns a new sorted list with the same elements as L."""
	print('In mergeSort. L =', L)
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L)//2
	left = mergeSort(L[:middle], compare)
	right = mergeSort(L[middle:], compare)
	return merge(left, right, compare)

mergeSort([1,3,5,5,4,2,42,5,6,7,9,8,8,7,6,5,2,1])

