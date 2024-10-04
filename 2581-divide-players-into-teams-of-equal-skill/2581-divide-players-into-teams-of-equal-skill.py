class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        l = 0
        r = n - 1
        total_skill = skill[l] + skill[r]
        res = 0
        while l < r:
            weak = skill[l]
            stronk = skill[r]
            summ = weak + stronk

            if summ != total_skill:
                return -1

            res += weak * stronk
            l += 1
            r -= 1
        
        return res