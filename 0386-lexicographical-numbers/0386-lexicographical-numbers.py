class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num):
            if num > n:
                return
            res.append(num)
            for i in range(10):
                next_num = num * 10 + i
                if next_num > n:
                    break
                dfs(next_num)
        
        for i in range(1, 10):
            dfs(i)
        
        return res