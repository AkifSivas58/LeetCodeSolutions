from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        freq = defaultdict(int)
        for x in arr:
            f = ((x%k) + k) % k
            freq[f] += 1
        
        for i in range(k-1):

            if i == k - i or i == 0:
                if freq[i] % 2 != 0:
                    return False
                continue

            if freq[i] != freq[k-i]:
                return False
        
        return True