# Set + Recursion Solution
# Time:     O(n * m),     Iterates through grid once.
# Space:    O(n * m),     Uses set to keep track of visited indices.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])                                          # Gets size of grid.        
        visited = set()                                                         # Set containing a tuple if indices visited in grid.
        
        def isValidIndice(row: int, column: int) -> bool:                       # Chekcs if a row and column are in the grid.
            if row < 0 or M <= row: return False                                # Checks for out of bounds row.
            if column < 0 or N <= column: return False                          # Checks for out of bounds column.
            
            return True                                                         # Returns True if all checks are passed.
        
        def islandArea(row, column) -> int:                                     # Gets the area of a 4-connected island on the grid. 
            if (row, column) in visited: return 0                               # Checks if indices have been visited already.
            if not isValidIndice(row, column): return 0                         # Checks if the indice is in bounds.
            if grid[row][column] == 0: return 0                                 # Checks if cell is water.
            
            visited.add((row, column))                                          # Adds cell to visited set.
            up, down = islandArea(row-1, column), islandArea(row+1, column)     # Recursive call to cells above and below to get area.
            left, right = islandArea(row, column-1), islandArea(row, column+1)  # Recursive call to cells left and right to get area.
            
            return 1 + up + down + left + right                                 # returns the area of the island.
            
            
        area, maxArea = 0, 0
        for row in range(M):                                                    # Iterates through grid rows.
            for column in range(N):                                             # Iterates through grid columns.
                area = islandArea(row, column)                                  # Gets area of island if cell is 1.
                maxArea = max(maxArea, area)                                    # Sets max island area found.
                
                
        return maxArea                                                          # Returns max island area found.


# Recursion Solution
# Time:     O(n * m),     Iterates through grid once.
# Space:    O(1),         Constant space used by mutating the input list to track visited cells.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])                                          # Gets size of grid.        
        
        
        def isValidIndice(row: int, column: int) -> bool:                       # Chekcs if a row and column are in the grid.
            if row < 0 or M <= row: return False                                # Checks for out of bounds row.
            if column < 0 or N <= column: return False                          # Checks for out of bounds column.
            
            return True                                                         # Returns True if all checks are passed.
        
        
        def islandArea(row, column) -> int:                                     # Gets the area of a 4-connected island on the grid. 
            if not isValidIndice(row, column): return 0                         # Checks if the indice is in bounds.
            if grid[row][column] == 0: return 0                                 # Checks if cell is water or has been visited.
            
            grid[row][column] = 0                                               # Sets cell value to 0 to indicate its been visited.                                        
            up, down = islandArea(row-1, column), islandArea(row+1, column)     # Recursive call to cells above and below to get area.
            left, right = islandArea(row, column-1), islandArea(row, column+1)  # Recursive call to cells left and right to get area.
            
            return 1 + up + down + left + right                                 # returns the area of the island.
            
            
        area, maxArea = 0, 0
        for row in range(M):                                                    # Iterates through grid rows.
            for column in range(N):                                             # Iterates through grid columns.
                area = islandArea(row, column)                                  # Gets area of island if cell is 1.
                maxArea = max(maxArea, area)                                    # Sets max island area found.
                
                
        return maxArea                                                          # Returns max island area found.