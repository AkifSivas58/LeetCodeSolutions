import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        events = []
        for i in range(n):
            arrival, leaving = times[i]
            events.append((arrival, "arrive", i))
            events.append((leaving, "leave", i))
        
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        chairs = list(range(n))
        heapq.heapify(chairs)

        occupied = dict()
        for time, event_type, friend in events:
            if event_type == "arrive":
                chair = heapq.heappop(chairs)
                occupied[friend] = chair

                if friend == targetFriend:
                    return chair
            elif event_type == "leave":
                chair = occupied[friend]
                heapq.heappush(chairs, chair)

