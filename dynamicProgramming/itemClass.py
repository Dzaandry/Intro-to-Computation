class Item(object):
	def __init__(self, n, v, w):
		self.name = n
		self.value = v
		self.weight = w
	def getName(self):
		return self.name
	
	def getValue(self):
		return self.value

	def getWeight(self):
		return self.weight

	def __str__(self):
		result = '<' + self.name + ', ' + str(self.value)\
			      + ', ' + str(self.weight) + '>'
		return result