from google.colab import files

class Solution:
    def countXMAS(self, grid):
        word = "XMAS"
        rows, cols = len(grid), len(grid[0])
        word_length = len(word)
        directions = [
            (0, 1),  # Right
            (0, -1),  # Left
            (1, 0),  # Down
            (-1, 0),  # Up
            (1, 1),  # Diagonal Down-Right
            (1, -1),  # Diagonal Down-Left
            (-1, 1),  # Diagonal Up-Right
            (-1, -1),  # Diagonal Up-Left
        ]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def search(x, y, dx, dy):
            """Check if 'XMAS' starts at (x, y) in the direction (dx, dy)."""
            for i in range(word_length):
                nx, ny = x + i * dx, y + i * dy
                if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                    return False
            return True

        count = 0
        for x in range(rows):
            for y in range(cols):
                for dx, dy in directions:
                    if search(x, y, dx, dy):
                        count += 1

        return count

uploaded = files.upload()

file_path = next(iter(uploaded))  
with open(file_path, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

solution = Solution()
result = solution.countXMAS(grid)
print("Total occurrences of 'XMAS':", result)

#PART TWO

class Solution:
    def countXMASPattern(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

    
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        
        for x in range(1, rows - 1):
            for y in range(1, cols - 1):
                if grid[x][y] == 'A':  
                    
                    if is_valid(x - 1, y - 1) and is_valid(x + 1, y + 1):
                        if (
                            grid[x - 1][y - 1] == 'M' and
                            grid[x + 1][y + 1] == 'S'
                        ) or (
                            grid[x - 1][y - 1] == 'S' and
                            grid[x + 1][y + 1] == 'M'
                        ):
                         
                            if is_valid(x - 1, y + 1) and is_valid(x + 1, y - 1):
                                if (
                                    grid[x - 1][y + 1] == 'M' and
                                    grid[x + 1][y - 1] == 'S'
                                ) or (
                                    grid[x - 1][y + 1] == 'S' and
                                    grid[x + 1][y - 1] == 'M'
                                ):
                                    count += 1 

        return count

uploaded = files.upload()

file_path = next(iter(uploaded)) 
with open(file_path, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

solution = Solution()
result = solution.countXMASPattern(grid)
print("Total occurrences of X-MAS:", result)