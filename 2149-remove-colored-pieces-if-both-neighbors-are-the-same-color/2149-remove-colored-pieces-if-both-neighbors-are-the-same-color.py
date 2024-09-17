class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        consec_a = 0
        consec_b = 0
        for c in colors:
            if c == 'A':
                consec_a += 1
                if consec_b > 2:
                    bob += consec_b - 2
                consec_b = 0
            else:
                consec_b += 1
                if consec_a > 2:
                    alice += consec_a - 2
                consec_a = 0

        if consec_b > 2:
            bob += consec_b - 2

        if consec_a > 2:
            alice += consec_a - 2

        if alice <= bob:
            return False
        else:
            return True
        