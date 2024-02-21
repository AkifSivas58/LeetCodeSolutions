class Solution(object):
    def majorityElement(self, nums):
        unique = list(set(nums))
        for num in unique:
            count = nums.count(num)
            if count > len(nums)/2:
                return num
        