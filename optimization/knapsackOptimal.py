# Straightforward approach:
# generate all subsets of the set of items - powerset
# remove all of the combinations whose weight exceeds the allowed weight
# from the remaining combinations choose any one whose value is the largest
# it's long! exponential complexity.

from knapsackGreedy import Item, value, weightInverse, density, buildItems

def chooseBest(pset, maxWeight, getVal, getWeight):
	bestVal = 0.0
	bestSet = None
	for items in pset:
		itemsVal = 0.0
		itemsWeight = 0.0
		for item in items:
			itemsVal += getVal(item)
			itemsWeight += getWeight(item)
		if (itemsWeight <= maxWeight) and (itemsVal > bestVal):
			bestVal = itemsVal
			bestSet = items
	return (bestSet, bestVal)