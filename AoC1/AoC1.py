f=open("input.txt")
pos=50
zeros=0
#Rewrote the cod with a ton of spaces lmao, I was losing my mind
for line in f:
    line.strip()
    if line[0]=='L':
        lastPos = pos
        clicks = int(line[1:])
        zeros +=  clicks // 100
        clicks %= 100
        pos = pos - clicks
        if pos < 0:
            pos += 100
            if lastPos > 0:
                zeros+=1

    if line[0]=='R':
        clicks = int(line[1:])
        zeros += clicks // 100
        clicks %= 100
        pos = pos + clicks
        if pos > 99:
            pos %= 100
            if pos>0:
                zeros += 1

    if pos == 0:
        zeros+=1



print(zeros)
## zad 2
# 50 : L150  zeros: 0
# 50 : lewo 50 zeros : 1
# 0  zeros 1
# 0  zeros 2

# 0: L 100
# 0 lewo 2
# -2
# 99 + 99 = 192