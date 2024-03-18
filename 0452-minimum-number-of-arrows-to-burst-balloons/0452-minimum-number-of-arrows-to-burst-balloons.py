class Solution(object):
    def findMinArrowShots(self, points):
        arrows = 0
        end = 0
        points.sort(key=lambda x : x[0])

        for point in points:
            if point[0] > end or end == 0:
                arrows += 1
                end = point[1]
            else:
                end = min(end, point[1])

        return arrows