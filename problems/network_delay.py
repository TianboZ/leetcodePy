class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        adj = {}  # <node, [ [node, cost], [node2, cost2],... ]>
        for node in range(1, n+1):
            adj[node] = []
        
        for a, b, t in times:
            adj[a].append([b, t])
        
        # init heap
        minheap = []
        visit = {} # <node, min cost>
        
        minheap.append([0, k])  # [cost from src, node]
        visit[k] = 0

        # terminate
        while minheap:
            # expand 
            curr= heapq.heappop(minheap)
            w1, n1 = curr
            
            # generate
            for nei in adj[n1]:
                n2, w2 = nei
                w = w1 + w2
                if n2 not in visit or w < visit[n2]:
                    visit[n2] = w
                    heapq.heappush(minheap, [w, n2])

        # already find min cost to reach all connectes nodes
        if len(visit) < n:
            # not possible
            return -1 

        print( visit.values())
        return max(visit.values())
        