class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        i = 0
        prof = 0
        res = 0
        for j in range(len(worker)):
            while i < len(jobs) and jobs[i][0] <= worker[j]:
                prof = max(prof, jobs[i][1])
                i += 1
            res += prof
        
        return res
        