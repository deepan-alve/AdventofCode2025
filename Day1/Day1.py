with open (r"C:\Users\deepa\Documents\Coding\AdventofCode2025\Day1\input.txt") as f :
    codes=f.readlines()
count=0
position=50
for code in codes :
    letter=code[0]
    distance=int(code[1:].strip())
    
    if letter == "R" :
        count += (position + distance) // 100
        position = (position + distance) % 100
    else :
        first_zero = position if position > 0 else 100
        if distance >= first_zero:
            count += 1 + (distance - first_zero) // 100
        position = (position - distance) % 100

print (count)