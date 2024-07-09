class Solution(object):
    def averageWaitingTime(self, customers):
        finish_time = 0
        res = 0
        for arrival, time in customers:
            if finish_time < arrival:
                finish_time = arrival + time
                res += time
            else:
                finish_time = finish_time + time
                waited = finish_time - arrival
                res += waited

        
        res = float(res) / len(customers)
        return res
        