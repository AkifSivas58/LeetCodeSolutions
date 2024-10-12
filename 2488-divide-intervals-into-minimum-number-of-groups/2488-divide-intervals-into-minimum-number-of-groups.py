class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        events.sort()

        curr = 0
        maxi = 0
        for time, event_type in events:
            curr += event_type
            maxi = max(curr, maxi)

        return maxi