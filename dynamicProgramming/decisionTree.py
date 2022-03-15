from itemClass import *
import random

# Complexity: O(2^n)
def maxVal(toConsider, avail):
	"""Assumes toConsider a list of items, avail a weight
	   Returns a tuple of the total value of a solution to
	   the 0/1 knapsack problem and the items of that solution"""
	if toConsider == [] or avail == 0:
		result = (0, ())
	elif toConsider[0].getWeight() > avail:
		result = maxVal(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = maxVal(toConsider[1:], avail - 
			                         nextItem.getWeight())
		withVal += nextItem.getValue()
		withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
		if withVal >= withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
	return result

#Pseudopolynomial complexity
def fastMaxVal(toConsider, avail, memo = {}):
	"""Assumes toConsider a list of items, avail a weight,
	   memo supplied by recursive calls
	   Returns a tuple of the total value of a solution to 0/1
	   knapsack problem and the items of that solution"""
	if (len(toConsider), avail) in memo:
		result = memo[(len(toConsider), avail)]
	elif toConsider == [] or avail == 0:
		result = (0, ())
	elif toConsider[0].getWeight() > avail:
		result = fastMaxVal(toConsider[1:], avail, memo)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = fastMaxVal(toConsider[1:], avail -
										nextItem.getWeight(), memo)
		withVal += nextItem.getValue()
		withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
		if withVal >= withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
	memo[(len(toConsider), avail)] = result
	return result
def smallTest():
	names = ['a', 'b', 'c', 'd']
	vals = [6, 7, 8, 9]
	weights = [3, 3, 2, 5]
	items = []
	for i in range(len(vals)):
		items.append(Item(names[i], vals[i], weights[i]))
	val, taken =  maxVal(items, 5)
	for item in taken:
		print(item)
	print('Total value of items taken =', val)

def buildManyItems(numItems, maxVal, maxWeight):
	items = []
	for i in range(numItems):
		items.append(Item(str(i), random.randint(1, maxVal),
						  random.randint(1, maxWeight)))
	return items

def bigTest(numItems):
	items = buildManyItems(numItems, 10, 10)
	val, taken = fastMaxVal(items, 40)
	print('Items taken')
	for item in taken:
		print(item)
	print('total value of items taken =', val) 

bigTest(10)