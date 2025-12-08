from os.path import split

file=open("input.txt")
#AGNES TACHYON <3
lines=[]
splits=0
for line in file: #To get list of chars instead of string... string is apparently immutable by string[x] operation lmao
    lines.append(list(line[:-1]))

for line in lines:
    for i in range(len(line)):
        if line[i] == '.':
            line[i] = 0


#{} dict? index: sum
beamSource=lines[0].index('S')
lines[1][beamSource]=1 #
copyLine=False
nextLine=[]
currentSplitters=[]
for lineIndex in range(2,len(lines)):
    row=lines[lineIndex]
    currentSplitters = {i for i, c in enumerate(row) if c == '^'}

    for char in range(len(row)):
        if char in currentSplitters:
            lines[lineIndex][char-1] += lines[lineIndex-1][char]
            lines[lineIndex][char+1] += lines[lineIndex-1][char]
        else:
            if lines[lineIndex-1][char] != '^':
                lines[lineIndex][char]+=lines[lineIndex-1][char]



    #
    # for splitter in currentSplitters:
    #     lines[lineIndex][splitter-1] += lines[lineIndex-1][splitter]
    #     lines[lineIndex][splitter+1] += lines[lineIndex-1][splitter]
    #
    #
    # for nonSplitter in notSplitters:
    #     if lines[lineIndex][nonSplitter]!='^':
    #         print(lines[lineIndex][nonSplitter])
    #         lines[lineIndex+1][nonSplitter]=lines[lineIndex][nonSplitter]

print(sum(lines[-1]))

