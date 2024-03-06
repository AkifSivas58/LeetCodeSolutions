class Solution(object):
    def isPathCrossing(self, path):
        coords = {(0, 0)}
        current_pos = [0, 0]

        for char in path:
            if char == "N":
                current_pos[1] += 1
            elif char == "E":
                current_pos[0] += 1
            elif char == "S":
                current_pos[1] -= 1
            elif char == "W":
                current_pos[0] -= 1
            
            if tuple(current_pos) in coords:
                return True
            else:
                coords.add(tuple(current_pos))
        
        return False