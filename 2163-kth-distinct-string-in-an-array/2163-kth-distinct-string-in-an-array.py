from collections import defaultdict
class Solution(object):
    def kthDistinct(self, arr, k):
        counts = defaultdict(int)
        for s in arr:
            counts[s] += 1

        count = 0
        for s in arr:
            if counts[s] == 1:
                count += 1

                if count == k:
                    return s
                
        return ""
        