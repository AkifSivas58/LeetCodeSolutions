class Solution(object):
    def maxDistance(self, arrays):
        res = 0
        maxi = arrays[0][-1]
        mini = arrays[0][0]
        for i in range(1, len(arrays)):
            cur_max = arrays[i][-1]
            cur_min = arrays[i][0]

            res = max(res, abs(cur_max - mini), abs(cur_min - maxi))

            maxi = max(cur_max, maxi)
            mini = min(cur_min, mini)

        return res