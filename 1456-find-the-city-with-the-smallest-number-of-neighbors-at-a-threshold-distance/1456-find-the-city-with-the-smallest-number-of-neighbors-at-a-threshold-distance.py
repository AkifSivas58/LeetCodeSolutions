from collections import defaultdict
import heapq

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        adj = defaultdict(list)
        for fr, to, w in edges:
            adj[fr].append((to, w))
            adj[to].append((fr, w))
        
        inf = float('inf')
        res = -1
        res_count = inf
        
        def dijkstra(node):
            pq = [(0, node)]
            dist = [inf] * n
            dist[node] = 0
            count = 0

            while pq:
                d, u = heapq.heappop(pq)
                
                for v, w in adj[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
                        
            for i in range(n):
                if i != node and dist[i] <= distanceThreshold:
                    count += 1

            return count
        
        for node in range(n):
            count = dijkstra(node)
            if count == res_count:
                res = max(res, node)
            elif count < res_count:
                res = node
                res_count = count
            
        return res
