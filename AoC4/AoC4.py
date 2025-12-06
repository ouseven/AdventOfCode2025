f=open("input.txt")
matrix=[]
for line in f:
    matrix.append(list(line[:-1]))
rangeY=len(matrix[0])
rangeX=len(matrix)
result=0
changed=True
while changed:
    changed=False
    for indexX in range(rangeX):
        for indexY in range(rangeY):
            if matrix[indexX][indexY]!='@':
                continue
            neighbours=0
            #Now to count all neighbours:
            for neighbourX in [-1,0,1]:
                for neighbourY in [-1,0,1]:
                    if 0 <= indexX+neighbourX < rangeX and 0 <= indexY + neighbourY < rangeY and  not (neighbourY==0 and neighbourX==0):
                        if matrix[indexX+neighbourX][indexY + neighbourY]=='@':
                            neighbours+=1
            if neighbours <4:
                result+=1
                matrix[indexX][indexY]='.'
                changed=True
print(result)


