class Solution(object):
    def strStr(self, haystack, needle):

        if len(haystack) < len(needle):
            return -1 
            
        l = 0
        r = 0
        ind = 0
        while l < len(haystack) and r < len(needle):
            if haystack[l] == needle[r]:
                tmp = l
                for st in haystack[l:]:
                    if st == needle[r]:
                        r += 1
                    else:
                        r = 0
                        break
                    
                    if r == len(needle):
                        return tmp
                l += 1
            else:
                l += 1
                r = 0
        
        return -1
            
            
        
        