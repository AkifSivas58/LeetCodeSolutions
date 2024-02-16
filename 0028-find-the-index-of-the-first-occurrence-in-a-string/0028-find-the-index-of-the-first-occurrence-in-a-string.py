class Solution(object):
    def strStr(self, haystack, needle):

        if len(needle) > len(haystack):
            return-1
            
        if needle == haystack:
            return 0
        
        for i in range(len(haystack)):
            j = 0
            tmp = ""
            char = haystack[i]
            if char == needle[j]:
                for t in haystack[i:]:

                    if t == needle[j]:
                        tmp = tmp + t
                        j += 1
                        if tmp == needle:
                            return i
                    else:
                        break

        return -1
        