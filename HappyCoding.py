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
			if not self.visited[i]:
				self.dfs(i)

	def sameComponent(self, i, j):
		return self.id[i] == self.id[j]

	def componentCount(self):
		return count

	def dfs_iterative(self, node):
		stack = [node]
		while stack:
			cur = stack.pop()
			self.visited[cur] = True
			neighbors = self.adjacency_list[cur]
			for i in neighbors:
				if not self.visited[i]:
					stack.append(i)

	# design a linear-time algorithm to find a vertex such that 
	# its maximum distance from any other vertex is minimized.
	def center(self):
		leaves = [i in range(self.num) if len(self.adjacency_list[i]) == 1]
		n = num 
		while n > 2:
			temp = []
			n -= len(leaves)
			for leaf in leaves:
				cur = self.adjacency_list[leaf]
				connected = cur.pop()
				self.adjacency_list[connected].remove(leaf)
				if len(self.adjacency_list[connected]) == 1:
					temp.append(connected)
			leaves = temp 
		return leaves



	# design a linear-time algorithm to find the longest simple path in the graph.
	# second solution: bfs find one end of longest path, then bsf from that end find
	# the other end of the longest path
	def diameter(self, node):
		if not node: return (0, 0) #(max_branch, cur_max)
		neighbors = self.adjacency_list[node]
		f = s = 0
		cur_max = 0
		for i in neighbors:
			b, t = self.diameter(i)
			cur_max = max(cur_max, t)
			if b > f:
				f, s = b, f
			elif b > s:
				s = b 
		return (max(f, s)+1, cur_max)
		


		

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

# find a cycle in udg
# find an edge connects current node to a visited node and the visited node is not its parent
class Undirect_find_cycle:
	def hasCycle(self, node, parent):
		self.visited[node] = True
		neighbors = self.adjacency_list[node]
		for i in neighbors:
			if not self.visited[i]:
				if self.hasCycle(i, node):
					return True
			elif i != parent:
				return True 
		return False 


# Euler cycle

# 