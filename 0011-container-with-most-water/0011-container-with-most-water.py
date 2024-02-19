class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1

        areas = []
        while l < r:

            if height[l] < height[r]:
                areas.append(height[l] * (r-l))
                l += 1
            else:
                areas.append(height[r] * (r-l))
                r -= 1

        return max(areas)
