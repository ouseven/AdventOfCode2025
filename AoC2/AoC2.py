f=open("input.txt")
ranges=[]
result=0
lowerBoundary=higherBoundary=divider=0
for line in f:
    ranges=line.split(',')
for boundary in ranges:
    boundary=boundary.split('-')
    lowerBoundary=int(boundary[0])
    higherBoundary=int(boundary[1])
    for index in range(lowerBoundary,higherBoundary+1):
        possibilities=[]
        repeatCount=0
        giftID=str(index)
        for possibility in range(1,len(giftID)//2+1):
            subGiftID=giftID[0:possibility]
            repeatCount=giftID.count(subGiftID)
            if repeatCount * len(subGiftID)==len(giftID):
                result+=index
                break
print(result)



