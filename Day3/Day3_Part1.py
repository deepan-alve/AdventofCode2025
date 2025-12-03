f = open(r"C:\Users\deepa\Documents\Coding\AdventofCode2025\Day3\input.txt")
data = f.read()
f.close()
lines = data.strip().split("\n")

ans = 0
for line in lines:
    max = 0
    for i in range(0, len(line)):
        for j in range(i+1, len(line)):
            num = int(line[i] + line[j])
            if num > max:
                max = num
    ans = ans + max

print(ans)
