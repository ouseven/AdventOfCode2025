def area(point1,point2):
    x1,y1=point1[0],point1[1]
    x2,y2=point2[0],point2[1]
    return (abs(x1-x2)+1)*(abs(y1-y2)+1)










file=open("input.txt")

points=[]
for line in file:
    row=line[:-1]
    row=row.split(',')
    points.append((int(row[0]),int(row[1])))

edges=[] #list of tuples : distance,point1,point2
for i in range(len(points)):
    for j in range(i+1,len(points)):
        edges.append( (area(points[i],points[j]),points[i],points[j]) )
edges.sort(reverse=True)


print(edges[0])
