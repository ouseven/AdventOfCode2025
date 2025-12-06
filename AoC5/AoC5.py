#WIP
f=open("input.txt")
IDRanges=[]
freshIDs=[]
ingredients=[]
result=0
divider=False
for line in f:
    if line=="\n":
        divider=True
        continue
    if not divider:
        IDRanges.append(line[:-1])
    else:
        ingredients.append(line[:-1])
for freshRange in IDRanges:
    freshRange=freshRange.split('-')
    lowerBoundary=int(freshRange[0])
    higherBoundary=int(freshRange[1])
    for i in range(lowerBoundary,higherBoundary+1):
        if i not in freshIDs:
            freshIDs.append(i)
for ingredient in ingredients:
    if int(ingredient) in freshIDs:
        result+=1
print(result)


