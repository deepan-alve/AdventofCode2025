f = open("input.txt", "r")
grid = [line.rstrip('\n') for line in f.readlines()]
f.close()

rows = len(grid)
cols = len(grid[0])

for col in range(cols):
    if grid[0][col] == 'S':
        start = col
        break

beams = set()
beams.add((0, start))

splits = 0

while beams:
    new_beams = set()
    
    for row, col in beams:
        next_row = row + 1
        
        if next_row >= rows:
            continue
        
        cell = grid[next_row][col]
        
        if cell == '.' or cell == 'S':
            new_beams.add((next_row, col))
        elif cell == '^':
            splits += 1
            left = col - 1
            right = col + 1
            if left >= 0:
                new_beams.add((next_row, left))
            if right < cols:
                new_beams.add((next_row, right))
    
    beams = new_beams

print(splits)
