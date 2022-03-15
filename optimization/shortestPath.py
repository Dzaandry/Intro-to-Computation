from graphClasses import *

def printPath(path):
	"""Assumes path is a list of nodes"""
	result = ''
	for i in range(len(path)):
		result += str(path[i])
		if i != len(path) - 1:
			result += '->'
	return result

#DFS - depth-first search, usually done recursively
def DFS(graph, start, end, path, shortest, toPrint = False):
	"""Assumes graph is a Digraph; start and end are nodes;
	   path and shortest are lists of nodes
	   Returns a shortest path from start to end in graph"""
	path = path + [start]
	if toPrint:
		print('Current DFS path:', printPath(path))
	if start == end:
		return path
	for node in graph.childrenOf(start):
		if node not in path:
			if shortest == None or len(path) < len(shortest):
				newPath = DFS(graph, node, end, path, shortest, toPrint)
				if newPath != None:
					shortest = newPath
	return shortest

def shortestPath(graph, start, end, toPrint = False):
	"""Assumes graph is a Digraph, start and end are nodes
	   Returns a shortest path from start to end in graph"""
	return DFS(graph, start, end, [], None, toPrint)

#BFS - breadth-first search, usually done iteratively
def BFS(graph, start, end, toPrint = False):
	"""Assumes graph is a Digraph, start and end are nodes
	   Returns a shortest path from start to end in graph"""
	initPath = [start]
	pathQueue = [initPath]

	while len(pathQueue) != 0:
		tmpPath = pathQueue.pop(0)
		print('Current BFS path:', printPath(tmpPath))
		if tmpPath[-1] == end:
			return tmpPath
		for nextNode in graph.childrenOf(tmpPath[-1]):
			if nextNode not in tmpPath:
				newPath = tmpPath + [nextNode]
				pathQueue.append(newPath)
	return None

def testSP():
	nodes = []
	for num in range(6):
		nodes.append(Node(str(num)))
	g = Digraph()
	for n in nodes:
		g.addNode(n)
	g.addEdge(Edge(nodes[0], nodes[1]))
	g.addEdge(Edge(nodes[1], nodes[2]))
	g.addEdge(Edge(nodes[2], nodes[3]))
	g.addEdge(Edge(nodes[2], nodes[4]))
	g.addEdge(Edge(nodes[3], nodes[4]))
	g.addEdge(Edge(nodes[3], nodes[5]))
	g.addEdge(Edge(nodes[0], nodes[2]))
	g.addEdge(Edge(nodes[1], nodes[0]))
	g.addEdge(Edge(nodes[3], nodes[1]))
	g.addEdge(Edge(nodes[4], nodes[0]))
	sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
	print('shortest path is', printPath(sp))
	sp = BFS(g, nodes[0], nodes[5])
	print('shortest path found by BFS:', printPath(sp))

testSP()


