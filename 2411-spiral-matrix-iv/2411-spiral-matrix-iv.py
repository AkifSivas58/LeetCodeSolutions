
class Solution(object):
    def spiralMatrix(self, m, n, head):
        # Initialize an m x n matrix filled with -1
        res = [[-1] * n for _ in range(m)]
        
        # Initialize boundaries for the spiral traversal
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Pointer to the current node in the linked list
        current = head
        
        while current:
            # Fill the top row from left to right
            for j in range(left, right + 1):
                if current:
                    res[top][j] = current.val
                    current = current.next
            top += 1  # Move the top boundary down
            
            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                if current:
                    res[i][right] = current.val
                    current = current.next
            right -= 1  # Move the right boundary left
            
            # Fill the bottom row from right to left
            if top <= bottom:  # Check if there is a valid row to fill
                for j in range(right, left - 1, -1):
                    if current:
                        res[bottom][j] = current.val
                        current = current.next
                bottom -= 1  # Move the bottom boundary up
            
            # Fill the left column from bottom to top
            if left <= right:  # Check if there is a valid column to fill
                for i in range(bottom, top - 1, -1):
                    if current:
                        res[i][left] = current.val
                        current = current.next
                left += 1  # Move the left boundary right
        
        return res
