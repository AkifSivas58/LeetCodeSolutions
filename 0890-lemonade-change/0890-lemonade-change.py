from collections import defaultdict
class Solution(object):
    def lemonadeChange(self, bills):
        changes = defaultdict(int)
        for bill in bills:
            changes[bill] += 1
            if bill == 10:
                if changes[5]:
                    changes[5] -= 1
                else:
                    return False
            elif bill == 20:
                if changes[10] and changes[5]:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True

        
        