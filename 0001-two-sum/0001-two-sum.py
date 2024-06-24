class Solution:
    def twoSum(self, nums, target):
        hashi = {}
        for i in range(len(nums)):
            hashi[nums[i]] = i
        
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in hashi:
                if hashi[tmp] == i:
                    continue
                return sorted([hashi[tmp], i])
            

            