class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]

        for i in range(1, n):
            pref[i] = pref[i-1] ^ nums[i]

        res = [0] * n
        for i in range(n):
            res[i] = pref[i] ^ 2 ** maximumBit - 1
        res.reverse()
        return res
