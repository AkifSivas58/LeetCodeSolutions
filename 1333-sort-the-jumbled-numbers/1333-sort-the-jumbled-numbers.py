class Solution(object):
    def sortJumbled(self, mapping, nums):
        mapped_nums = []
        for i, num in enumerate(nums):
            new_num = ""
            for c in str(num):
                mapp = mapping[int(c)]
                new_num += str(mapp)
            mapped_nums.append((int(new_num), i, num))
        
        # Sort based on the transformed number and use the original index as a tiebreaker
        mapped_nums.sort()
        
        # Extract the original numbers in the new order
        sorted_nums = [num for _, _, num in mapped_nums]
        
        return sorted_nums
