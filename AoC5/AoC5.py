#WIP
f=open("input.txt")
IDRanges=[]
mergedRanges=[]
ingredients=[]
result=left=right=0
freshIDsCount=0
divider=False
for line in f:
    if line=="\n":
        divider=True
        continue
    if not divider:
        IDRanges.append( [int((line[:-1]).split('-')[0]), int((line[:-1]).split('-')[1]) ] )
    else:
        ingredients.append(int(line[:-1]))
IDRanges=sorted(IDRanges, key=lambda x: x[0])
left = int(IDRanges[0][0])
right = int(IDRanges[0][1])
for nextLeft,nextRight in IDRanges[1:]:
    if right + 1 < nextLeft: # 0: [1,4] [5,20]  -> [1,20];  [1,4] [7,10] -> [1,4] [7,10]
        mergedRanges.append([left,right])
        left=nextLeft
        right=nextRight
    elif right + 1 >=  nextLeft:
        #left stays the same, right gets updated
        right=max(right,nextRight)
mergedRanges.append([left, right])

for ingredientIndex in range(len(ingredients)):
    for freshRange in mergedRanges:
        if freshRange[1] >= int (ingredients[ingredientIndex]) >= freshRange[0]:
            result+=1
            ingredientIndex+=1
            break
for freshRange in mergedRanges:
    freshIDsCount+=freshRange[1]-freshRange[0]+1


print(result)
print(freshIDsCount)


