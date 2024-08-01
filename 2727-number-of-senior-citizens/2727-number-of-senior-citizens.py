class Solution(object):
    def countSeniors(self, details):
        res = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                res += 1
        
        return res
        