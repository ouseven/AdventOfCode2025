import math

#DISCLAIMER: this code isn't really mine per se, I heavily copied what has been said on lectures regarding graphs, especially MST.

class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size= [1] * n
    def Find(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def Union(self,x,y):
        x=self.Find(x)
        y=self.Find(y)
        if x==y:
            return False
        if self.size[x] < self.size[y]:
            x,y=y,x
        self.parent[y]=x
        self.size[x] += self.size[y]
        return True

def euclideanDistance(x,y):
    temp=0
    for i in range(3):
        temp+=(x[i]-y[i])**2
    return math.sqrt(temp)


file=open("input.txt")
points=[]
for line in file:
    points.append(list (line[:-1].split(',')))

for point in range(len(points)):
    for number in range(len(points[point])):
        points[point][number]=int(points[point][number])

print(points)
edges=[] # (distance : i,j) tuple
circuits={}
connections=0
for i in range(len(points)):
    for j in range(i+1,len(points)):
        edges.append((euclideanDistance(points[i],points[j]),i,j,points[i][0],points[j][0]))
edges.sort()
dsu=DSU(len(points))

#connect untill they all have the same root?
#so.. connect every vertice... that's 999 operations.
#gotta keep track of how many have been merged
#and if it is the 998th operation, get the result
successes=0
needed=999
for edge in edges:
    dist,i,j,ix,jx=edge
    if dsu.Union(i,j):
        successes+=1
        if successes==999:
            print(ix*jx)
            break
