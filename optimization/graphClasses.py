class Node(object):
	def __init__(self, name):
		"""Assumes name is a string"""
		self.name = name

	def getName(self):
		return self.name

	def __str__(self):
		return self.name

class Edge(object):
	def __init__(self, src, dest):
		"""Assumes src and dest are Nodes"""
		self.src = src
		self.dest = dest

	def getSource(self):
		return self.src
	
	def getDestination(self):
		return self.dest
	def __str__(self):
		return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
	def __init__(self, src, dest, weight = 1.0):
		"""Assumes src and dest are nodes, weight a number"""
		self.src =  src
		self.dest = dest
		self.weight = weight
	
	def getWeight(self):
		return self.weight

	def __str__(self):
		return self.src.getName() + '->(' + str(self.weight) + ')'\
				+ self.dest.getName()


class Digraph(object):
	#nodes is a list of the nodes in the graph
	#edges is a dict mapping each node to a list of its children
	def __init__(self):
		self.nodes = []
		self.edges = {}

	def addNode(self, node):
		if node in self.nodes:
			raise ValueError('Duplicate node!')
		else:
			self.nodes.append(node)
			self.edges[node] = []

	def addEdge(self, edge):
		src = edge.getSource()
		dest = edge.getDestination()
		if not (src in self.nodes and dest in self.nodes):
			raise ValueError('node not in graph!')
		self.edges[src].append(dest)

	def childrenOf(self, node):
		return self.edges[node]

	def hasNode(self, node):
		return node in self.nodes

	def __str__(self):
		result = ''
		for src in self.nodes:
			for dest in self.edges[src]:
				result = result + src.getName() + '->'\
								+ dest.getName() + '\n'
		return result[:-1]	 #omit final newline

class Graph(Digraph):
	def addEdge(self, edge):
		Digraph.addEdge(self, edge)
		rev = Edge(edge.getDestination(), edge.getSource())
		Digraph.addEdge(self, rev)

# Why digraph is the superclass?
# substitution principle: if client code works correctly with an instance
# of the supertype, it should also work correctly when an instance
# of the subtype is substituted for the instance of the supertype
#There are many algos that work on graphs, but do not work on directed graphs.