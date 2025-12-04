f = open(r"C:\Users\deepa\Documents\Coding\AdventofCode2025\Day4\input.txt")
data = f.read()
f.close()
grid = data.strip().split("\n")

rows = len(grid)
cols = len(grid[0])

count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbors = neighbors + 1
            if neighbors < 4:
                count = count + 1

print(count)
