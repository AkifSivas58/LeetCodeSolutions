class Solution:
    def maximumSwap(self, num: int) -> int:
        st = str(num)
        n = len(st)

        max_right_ind = [0] * n
        max_right_ind[n-1] = n-1
        for i in range(n-2, -1, -1):
            if st[i] > st[max_right_ind[i + 1]]:
                max_right_ind[i] = i
            else:
                max_right_ind[i] = max_right_ind[i+1]
            
        for i in range(n):
            if st[i] < st[max_right_ind[i]]:
                st = list(st)
                st[i], st[max_right_ind[i]] = st[max_right_ind[i]], st[i]
                return int("".join(st))
        
        return num

