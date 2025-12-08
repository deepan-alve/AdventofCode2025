f = open("input.txt")
points = []
for line in f:
    x, y, z = map(int, line.strip().split(','))
    points.append((x, y, z))
f.close()

n = len(points)

dists = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        d = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
        dists.append((d, i, j))

dists.sort()

parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py
        return True
    return False

circuits = n
for d, a, b in dists:
    if union(a, b):
        circuits -= 1
        if circuits == 1:
            print(points[a][0] * points[b][0])
            break
