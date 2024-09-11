class Solution(object):
    def minBitFlips(self, start, goal):
        xor = start ^ goal
        ones = bin(xor).count('1')
        return ones