class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        n = len(distance)
        res1 = 0
        curr = start
        while curr != destination:
            res1 += distance[curr]
            curr = (curr + 1) % n
        
        res2 = 0
        curr = destination
        while curr != start:
            res2 += distance[curr]
            curr = (curr + 1) % n
        
        return min(res1, res2)
        