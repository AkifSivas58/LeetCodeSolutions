from collections import defaultdict
class Solution(object):
    def canBeEqual(self, target, arr):
        if arr == target:
            return True
        
        nums = defaultdict(int)

        for num in arr:
            nums[num] += 1
        
        for num in target:
            if nums[num] == 0:
                return False
            else:
                nums[num] -= 1

        return True