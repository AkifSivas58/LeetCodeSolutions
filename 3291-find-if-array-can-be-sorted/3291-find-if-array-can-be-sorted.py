class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def setbits(n):
            count = 0
            while n:
                count += n & 1
                n = n >> 1
            return count
        
        prev_max = 0
        curr_max = 0
        bits = 0
        curr_small = float('inf')

        for num in nums:
            if setbits(num) != bits:
                prev_max = max(prev_max, curr_max)
                curr_small = num
                curr_max = num
                bits = setbits(num)
            
            curr_small = min(curr_small, num)
            curr_max = max(curr_max, num)
            
            if curr_small < prev_max:
                return False
            
            
        
        return True
            