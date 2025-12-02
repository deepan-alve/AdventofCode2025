with open(r"C:\Users\deepa\Documents\Coding\AdventofCode2025\Day2\input.txt") as f:
    line = f.read().strip()

ranges = []
for part in line.split(","):
    part = part.strip()
    if part:
        start, end = part.split("-")
        ranges.append((int(start), int(end)))

def find_invalid(start, end):
    invalid = set()
    min_dig = len(str(start))
    max_dig = len(str(end))
    
    for n in range(min_dig, max_dig + 1):
        for rlen in range(1, n):
            if n % rlen != 0:
                continue
            if rlen == 1:
                pstart = 1
            else:
                pstart = 10 ** (rlen - 1)
            pend = 10 ** rlen - 1
            reps = n // rlen
            
            for p in range(pstart, pend + 1):
                s = str(p)
                num = int(s * reps)
                if start <= num <= end:
                    invalid.add(num)
    return invalid

total = 0
for start, end in ranges:
    ids = find_invalid(start, end)
    total += sum(ids)

print(total)
