
# Linear complexity: O(len(L))

def simpleSearch(L, e):
	"""Assumes L is a list.
	   Returns true if e is in L and False otherwise."""
	for i in range(len(L)):
		if L[i] == e:
			return True
	return False

# Linear search of  a sorted list:

def search1(L, e):
	"""Assumes L is a list, the elements of which are sorted in ascending order.
	   Returns True if e is in L and False otherwise."""
	for i in range(len(L)):
		if L[i] == e:
			return True
		if L[i] > e:
			return False
	return False

# Recursive binary search: O(log(len(L) - 1)) complexity

def search2(L, e):
	"""Assumes L is a list, the elements of which are sorted
	   in ascending order.
	   Returns True if e is in L and False otherwise."""
	def binSearch(L, e, low, high):
		print('low=', low, 'high=', high)
		if low == high:
			return L[low] == e
		mid = (low + high) // 2
		if L[mid] == e:
			return True
		elif L[mid] > e:
			if low == mid:
				return False
			else:	
				return binSearch(L, e, low, (mid - 1))
		else:
			return binSearch(L, e, (mid + 1), high)  
	if len(L) == 0:
		return False
	return binSearch(L, e, 0, (len(L) - 1))

print(search2([1,2,3,4,5,6,7], 1))
print(search2([1,2,3,4,5,6,7], 2))
print(search2([1,2,3,4,5,6,7], 3))
print(search2([1,2,3,4,5,6,7], 4))
print(search2([1,2,3,4,5,6,7], 5))
print(search2([1,2,3,4,5,6,7], 6))
print(search2([1,2,3,4,5,6,7], 7))
print(search2([1,2,3,4,5,6,7], 4.5))
print(search2([1,2,3,4,5,6,7], 8))
print(search2([1,2,3,4,5,6,7], 0))