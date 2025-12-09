import time
def area(point1,point2):
    x1,y1=point1[0],point1[1]
    x2,y2=point2[0],point2[1]
    return (abs(x1-x2)+1)*(abs(y1-y2)+1)


file=open("example.txt")

points=[]
for line in file:
    row=line[:-1]
    row=row.split(',')
    points.append([int(row[0]),int(row[1])])



lines=[] #list of tuples : distance,point1,point2
for i in range(len(points)):
    for j in range(i+1,len(points)):
        if points[i][0]==points[j][0] or points[i][1]==points[j][1]:
            lines.append( [points[i],points[j]] ) #but, we'd need to sort them out first. prefferably by Y's of the first point.

#Approach: Let leftboundary x of first point of line, second boundary = x of second point of line. If we meet another point stop (left or right boundary already in lines.)
# first [] -> which line
# second [] -> 0 for first and 1 for second point of line
# third [] -> 0 for x and 1 for y 
finalLines=lines[:]
sortedLines=sorted(lines, key=lambda x: x[0][1])


leftBoundary=[sortedLines[0][0][0],sortedLines[0][0][1]] 
rightBoundary=[sortedLines[0][1][0],sortedLines[0][1][1]]
changeLeft=False
changeRight=False
for line in sortedLines:
    if changeLeft:
        leftBoundary=[line[0][0],line[0][1]]
        changeLeft=False
        
    if changeRight:
        rightBoundary=[line[1][0],line[1][1]]
        changeRight=False

    if line[0][1]==line[1][1]: #only vertical lines
        leftBoundary[1]+=1
        rightBoundary[1]+=1

        while leftBoundary not in points and rightBoundary not in points:
            tempLine=[leftBoundary[:],rightBoundary[:]]
            finalLines.append(tempLine)
            print(tempLine)
            leftBoundary[1]+=1
            rightBoundary[1]+=1
            
            time.sleep(1)
        
        if  leftBoundary in points:
            changeLeft=True
        if rightBoundary in points:
            changeRight=True

sortedLines=sorted(lines, key=lambda x: x[0][0])
upperBoundary=[sortedLines[0][0][0],sortedLines[0][0][1]]
lowerBoundary=[sortedLines[0][1][0],sortedLines[0][1][1]] 
changeUp=False
changeDown=False
for line in sortedLines:
    if changeUp:
        upperBoundary=[line[0][0],line[0][1]]
        changeUp=False
    if changeDown:
        lowerBoundary=[line[0][0],line[0][1]]
        changeDown=False

    if line[0][0]==line[1][0]: #only vertical lines
        upperBoundary[1]+=1
        lowerBoundary[1]+=1
        while lowerBoundary not in points and upperBoundary not in points:
            tempLine=[lowerBoundary,upperBoundary]
            finalLines.append(tempLine)
            lowerBoundary[1]+=1
            upperBoundary[1]+=1
        if lowerBoundary in points:
            changeDown=True
        if upperBoundary in points:
            changeUp=True

print(len(finalLines)-len(sortedLines))
















# for i in range(len(sortedLines)):
#     if sortedLines[i][0][0]==sortedLines[i][1][0]: #this if is for vertical lines
#         #we switch the boundary when it is in points.
#         if leftBoundary in points:
#             rightBoundary[1]+=1
#             leftBoundary=(sortedLines[i][0][0],sortedLines[i][0][1]+1) 
#         if rightBoundary in points:
#             leftBoundary[1]+=1
#             rightBoundary=(sortedLines[i][1][0],sortedLines[i][1][1]+1)
#         while tuple(rightBoundary) not in points and tuple(leftBoundary) not in points:
#             finalLines.append((leftBoundary,rightBoundary))
#             rightBoundary[1]+=1
#             leftBoundary[1]+=1

#     if sortedLines[i][0][1]==sortedLines[i][1][1]:#this if is for the horizontal ones.
#         if lowerBoundary in points:
#             upperBoundary[0]+=1
#             lowerBoundary=(sortedLines[i][0][0],sortedLines[i][0][1]+1) 
#         if upperBoundary in points:
#             lowerBoundary[0]+=1
#             upperBoundary=(sortedLines[i][1][0],sortedLines[i][1][1]+1)
#         while tuple(upperBoundary) not in points and tuple(lowerBoundary) not in points:
#             finalLines.append((lowerBoundary,upperBoundary))
#             upperBoundary[0]+=1
#             lowerBoundary[0]+=1


        #old approach, didn't work.

    # if sortedLines[i][0][0]==sortedLines[j][0][0] and sortedLines[i][1][0]==sortedLines[j][1][0]: #Make lines only if we can make lines of same size as original ones
    #     nextLine=1
    #     tempLine=((sortedLines[i][0][0],sortedLines[i][0][1]+nextLine),(sortedLines[i][1][0],sortedLines[i][1][1]+nextLine))
    #     print(tempLine)
    #     print(sortedLines[j])
    #     while tempLine!= sortedLines[j] : #stop when next line is met
    #         finalLines.append(tempLine)
    #         nextLine+=1
    #         tempLine=((sortedLines[i][0][0],sortedLines[i][0][1]+nextLine),(sortedLines[i][1][0],sortedLines[i][1][1]+nextLine))



