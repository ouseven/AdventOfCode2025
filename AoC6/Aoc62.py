from math import prod


f=open("input.txt")
operations=[]
lines=[]
columns=[]
numbers=[]
grandValue=indexY=0
metNextOperator=False
for line in f:
    line=line.rstrip('\n')
    if line[0]=='*' or line[0]=="+":
        for operator in line:
            if operator!=' ':
                operations.append(operator)
    lines.append(line)

#if last element in column is an operator it means that there is a new number. first column -> met an operator
while indexY < len(lines[0]):
    firstCol=True
    while indexY < len (lines[0]) and (firstCol or lines[4][indexY] ==' '):
        firstCol=False
        number=""
        for digit in range(4):
            if lines[digit][indexY]!=' ':
                number+=lines[digit][indexY]
        if len(number)>0:
            indexY+=1
            numbers.append(int(number))
        else:
            if len(numbers)>0:
                columns.append(numbers[:])
            numbers=[]
            firstCol=True
            indexY+=1
            break
columns.append(numbers)


print(operations)
print(len(columns))


for operator in range(len(operations)):
    if operations[operator] == '*':
        grandValue+= prod (columns[operator])
    elif operations[operator] == '+':
        grandValue+= sum(columns[operator])
print(grandValue)
