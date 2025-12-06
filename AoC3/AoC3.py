f=open("input.txt")
totalJoltage=0
firstDigit=secondDigit=end=maximum=0
startPos=0
digits=[]
for line in f:
    bank=line[:-1]
    startPos=0
    for digit in range(12):
        end=-11+digit
        if end!=0:
            maximum=max(bank[startPos:end])
        else:
            maximum=max(bank[startPos:]) # 11: 0
        digits.append(maximum)
        startPos=bank.index(maximum,startPos)+1
        totalJoltage+=int(maximum) * (10 **(11-digit))
print(totalJoltage)


