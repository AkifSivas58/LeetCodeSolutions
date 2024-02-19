class Solution(object):
    def isLongPressedName(self, name, typed):
        i = 0
        j = 0
        if name == typed:
            return True
        
        while j < len(typed):
                if i < len(name) and name[i] == typed[j]:
                    i += 1
                    j += 1
                elif j > 0 and typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False

        return i == len(name)