class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for n in range(len(nums)-1, 0, -1):
            for i in range(n):
                str1 = str(nums[i]) + str(nums[i+1])
                str2 = str(nums[i+1]) + str(nums[i])
                if int(str1) > int(str2):
                    nums[i], nums[i+1] = nums[i+1], nums[i]

        res = "".join(map(str, reversed(nums)))
        
        if res and res[0] == "0":
            res = "0"

        return res