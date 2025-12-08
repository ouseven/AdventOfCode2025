from math import prod

f=open("input.txt")
operations=[]
lines=[]
columns=[]
grandValue=0
for line in f:
    line=line.strip()
    print(line)
    numbers=[]
    number = ""
    if line[0]!="*" and line[0]!="+":
        for digit in line:
            if digit==' ':
                if len(number)>0:
                    numbers.append(int(number))
                number=""
                continue
            else:
                number+=digit
        numbers.append(int(number))
    else:
        for operator in line:
            if operator!=' ':
                operations.append(operator)
    lines.append(numbers)
lines=lines[:-1]
for index in range(len(operations)):
    column=[lines[0][index],lines[1][index],lines[2][index],lines[3][index]]
    if operations[index]=='*':
        grandValue+= prod(column)
    if operations[index]=='+':
        grandValue+= sum(column)

print(grandValue)
