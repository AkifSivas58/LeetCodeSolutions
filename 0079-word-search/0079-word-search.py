class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, ind):
            if i >= m: return False
            if i < 0: return False
            if j >= n: return False
            if j < 0: return False

            if word[ind] == board[i][j]:
                if ind + 1 == len(word):
                    return True
            else:
                return False
            
            tmp = board[i][j]
            board[i][j] = "!"
            res = dfs(i+1, j, ind+1) or dfs(i-1, j, ind+1) or dfs(i, j+1, ind+1) or dfs(i, j-1, ind+1)
            board[i][j] = tmp
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
            
            