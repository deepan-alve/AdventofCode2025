f = open(r"C:\Users\deepa\Documents\Coding\AdventofCode2025\Day3\input.txt")
data = f.read()
f.close()
lines = data.strip().split("\n")

ans = 0
for line in lines:
    n = len(line)
    res = []
    start = 0
    for x in range(12):
        need = 12 - x
        end = n - need + 1
        bestidx = start
        bestdig = line[start]
        for i in range(start, end):
            if line[i] > bestdig:
                bestdig = line[i]
                bestidx = i
        res.append(bestdig)
        start = bestidx + 1
    num = int("".join(res))
    ans = ans + num

print(ans)
