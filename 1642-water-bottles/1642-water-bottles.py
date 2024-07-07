class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        res = 0
        empty = 0
        while numBottles != 0:
            empty += numBottles
            res += numBottles

            numBottles = 0
            toAdd = empty // numExchange
            empty = empty % numExchange
            numBottles += toAdd

        return res