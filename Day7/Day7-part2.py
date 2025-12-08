from functools import lru_cache

f = open("input.txt", "r")
lines = f.read().rstrip('\n').split('\n')
f.close()

grid = tuple(line for line in lines if line.strip())
rows = len(grid)
cols = len(grid[0])

for col in range(cols):
    if grid[0][col] == 'S':
        start = col
        break

@lru_cache(maxsize=None)
def count(row, col):
    next_row = row + 1
    
    if next_row >= rows:
        return 1
    
    cell = grid[next_row][col]
    
    if cell == '.' or cell == 'S':
        return count(next_row, col)
    elif cell == '^':
        total = 0
        left = col - 1
        right = col + 1
        
        if left >= 0:
            total += count(next_row, left)
        else:
            total += 1
        
        if right < cols:
            total += count(next_row, right)
        else:
            total += 1
        
        return total
    else:
        return count(next_row, col)

print(count(0, start))
