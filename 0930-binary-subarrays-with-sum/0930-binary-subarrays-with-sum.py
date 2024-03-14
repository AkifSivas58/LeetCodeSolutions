class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        current_sum = 0
        res = 0
        prefix_sum = {0 : 1}
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if (current_sum - goal) in prefix_sum:
                res += prefix_sum[current_sum - goal]

            prefix_sum[current_sum] =  prefix_sum.get(current_sum, 0) + 1


        return res 