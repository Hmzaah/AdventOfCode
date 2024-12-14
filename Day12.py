
def read_map(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, grid, visited):
    stack = [(x, y)]
    visited[y][x] = True
    region_char = grid[y][x]
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()
        area += 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == region_char and not visited[ny][nx]:
                    visited[ny][nx] = True
                    stack.append((nx, ny))
                elif grid[ny][nx] != region_char:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter

def calculate_fencing_price(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total_price = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if not visited[y][x]:
                area, perimeter = dfs(x, y, grid, visited)
                total_price += area * perimeter

    return total_price

from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]

garden_map = read_map(file_name)
result = calculate_fencing_price(garden_map)
print("Total price of fencing all regions:", result)
