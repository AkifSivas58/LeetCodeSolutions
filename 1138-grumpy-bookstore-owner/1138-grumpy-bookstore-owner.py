class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        satisfied = 0
        n = len(customers)
        
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
        
        satisfieable = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                satisfieable += customers[i]
        
        maxi = satisfieable
        
        for i in range(minutes, n):
            if grumpy[i] == 1:
                satisfieable += customers[i]
            if grumpy[i - minutes] == 1:
                satisfieable -= customers[i - minutes]
            
            maxi = max(maxi, satisfieable)
        
        return satisfied + maxi
