# Given a undirected graph, find all connected components
class CONNECTED_COMPONENT:
	def __init__(self, num, adjacency_list):
		self.count = 0
		self.num = num
		self.adjacency_list = adjacency_list
		self.visited = [False]*num
		self.id = [-1]*num
		
	def run(self):
		for i in range(self.num):
			if not self.visited[i]:
				self.dfs(i)
				self.count += 1

	def dfs(self, node):
		self.visited[node] = True
		self.id[node] = self.count
		neighbors = self.adjacency_list[node]
		for i in neighbors:
			if not visited[i]:
				self.dfs(i)

	def sameComponent(self, i, j):
		return self.id[i] == self.id[j]

	def componentCount(self):
		return count

# bfs approach for bipartite problem
class Bipartile:
	def __init__(self, num, adjacency_list):
		self.num = num
		self.adjacency_list = adjacency_list
		self.color = [-1]*num

	def run(self):
		q = [0]
		self.color[0] = 0
		color = 0 
		while q:
			node = q.pop(0)
			neighbors = self.adjacency_list[node]
			for i in neighbors:
				if i == node:
					return False
				if self.color[i] == -1:
					self.color[i] = 1-color
					q.append(i)
				elif self.color[i] == self.color[node]
						return False
			color = 1-color
		return True





