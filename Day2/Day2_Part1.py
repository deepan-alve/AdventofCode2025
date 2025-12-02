with open(r"C:\Users\deepa\Documents\Coding\AdventofCode2025\Day2\input.txt") as f:
    line = f.read().strip()

ranges = []
for part in line.split(","):
    part = part.strip()
    if part:
        start, end = part.split("-")
        ranges.append((int(start), int(end)))

def find_invalid(start, end):
    invalid = []
    min_dig = len(str(start))
    max_dig = len(str(end))
    
    for n in range(min_dig, max_dig + 1):
        if n % 2 != 0:
            continue
        half = n // 2
        if half == 1:
            pstart = 1
        else:
            pstart = 10 ** (half - 1)
        pend = 10 ** half - 1
        
        for p in range(pstart, pend + 1):
            s = str(p)
            num = int(s + s)
            if start <= num <= end:
                invalid.append(num)
    return invalid

total = 0
for start, end in ranges:
    ids = find_invalid(start, end)
    total += sum(ids)

print(total)
