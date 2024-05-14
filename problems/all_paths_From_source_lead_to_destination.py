'''
solution:
if has cycle, return false
since could have cycle, creat a hashset to record what nodes have been visited


'''

from typing import List


class Solution:
  def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
		visit = set()
		graph = self.get_graph(edges)
		return self.dfs(source, graph, visit, destination)

	def get_graph(self, edges):
		map = {}
		for a, b in edges:
			if map.get(a):
				map[a].append(b)
			else:
				map[a] = [b]
		print(map)
		return map
    
	# return false if can't reach to target 
	def dfs(self, node, graph, visit, target):
		# basecase
		if node in visit:
			return False
		
		if node == target:
			return True

		# recursive rule
		visit.add(node)
		for nei in graph[node]:
			if not self.dfs(nei, graph, visit, target):
				return False
		visit.remove(node)

		return True  
	

sol = Solution()
res = sol.leadsToDestination(4, [[0,1],[0,3],[1,2],[2,1]], 0, 3)
print(res)