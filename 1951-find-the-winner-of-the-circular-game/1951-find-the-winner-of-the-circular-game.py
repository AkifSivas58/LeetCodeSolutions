class Solution(object):
    def findTheWinner(self, n, k):
        players = list(range(1, n+1))
        i = -1
        while len(players) > 1:
            for _ in range(k):
                i += 1
                if i == len(players):
                    i = 0
            players.pop(i)
            i -= 1
        return players[0]