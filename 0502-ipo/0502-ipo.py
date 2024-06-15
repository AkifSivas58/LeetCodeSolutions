import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        cap = w
        maxi_profi = []
        for _ in range(k):
            while projects and projects[0][0] <= cap:
                capi, profi = projects.pop(0)
                heapq.heappush(maxi_profi, (-profi, capi))

            if not maxi_profi:
                break
            
            cap += -heapq.heappop(maxi_profi)[0]
        
        return cap
