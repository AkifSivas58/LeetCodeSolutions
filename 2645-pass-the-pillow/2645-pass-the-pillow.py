class Solution(object):
    def passThePillow(self, n, time):
        direction = 1
        i = 1
        while time > 0:
            if direction == 1:
                i += 1
            else:
                i -= 1
            if i == n or i == 1:
                direction *= -1
            
            time -= 1
        return i