class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tmp = sorted(arr)
        ranks = dict()
        cur = 1
        for num in tmp:
            if num not in ranks.keys():
                ranks[num] = cur
                cur += 1
            else:
                ranks[num] = cur - 1
        
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        
        return arr


