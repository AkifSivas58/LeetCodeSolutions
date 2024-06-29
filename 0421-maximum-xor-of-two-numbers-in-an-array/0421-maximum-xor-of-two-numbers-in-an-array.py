class Solution(object):
    class Trie:
        def __init__(self):
            self.root = {}
        
        def insert(self, num):
            node = self.root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        def find_max_xor(self, num):
            node = self.root
            max_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit

                if toggled_bit in node:
                    max_xor = (max_xor << 1) | 1
                    node = node[toggled_bit]
                else:
                    max_xor = (max_xor << 1) | 0
                    node = node[bit]
            return max_xor

    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask |= (1 << i)
            found_prefixes = set([num & mask for num in nums])
            
            potential_max_xor = max_xor | (1 << i)
            found = False
            
            for prefix in found_prefixes:
                if (prefix ^ potential_max_xor) in found_prefixes:
                    found = True
                    break
            
            if found:
                max_xor = potential_max_xor
        
        return max_xor
    
