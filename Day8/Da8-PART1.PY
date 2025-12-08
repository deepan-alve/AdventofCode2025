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

for i in range(1000):
    d, a, b = dists[i]
    union(a, b)

sizes = {}
for i in range(n):
    p = find(i)
    sizes[p] = sizes.get(p, 0) + 1

top3 = sorted(sizes.values(), reverse=True)[:3]
print(top3[0] * top3[1] * top3[2])
