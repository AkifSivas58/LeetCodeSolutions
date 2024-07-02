class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        l = 0
        r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                res.append(nums1[l])
                l += 1
                r += 1
            
        return res
        