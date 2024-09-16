class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for c in timePoints:
            hour = int(c[:2])
            minute = int(c[3:])
            minutes.append(hour * 60 + minute)
        
        minutes.sort()
        mini = abs(minutes[0] + 1440 - minutes[-1])
        for i in range(1, len(minutes)):
            mini = min(mini, abs(minutes[i] - minutes[i-1]))

        return mini        
