class Solution(object):
    def tictactoe(self, moves):
        grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for i in range(len(moves)):
            if i % 2 == 0:
                grid[moves[i][0]][moves[i][1]] = 'X'
            else:
                grid[moves[i][0]][moves[i][1]] = 'O'

        for i in range(len(grid)):
            places = {'X': 0, 'O': 0}
            for j in range(len(grid)):
                if grid[i][j] == 'X':
                    places['X'] += 1
                elif grid[i][j] == 'O':
                    places['O'] += 1

                if places['X'] == 3:
                    return "A"
                elif places['O'] == 3:
                    return "B"

        for i in range(len(grid[0])):
            places = {'X': 0, 'O': 0}
            for j in range(len(grid)):
                if grid[j][i] == "X":
                    places['X'] += 1
                elif grid[j][i] == "O":
                    places['O'] += 1
                
                if places['X'] == 3:
                    return "A"
                elif places['O'] == 3:
                    return "B"
            
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            if grid[0][0] == 'X':
                return "A"
            elif grid[0][0] == "O":
                return "B"

        if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
            if grid[1][1] == 'X':
                return "A"
            elif grid[1][1] == "O":
                return "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"