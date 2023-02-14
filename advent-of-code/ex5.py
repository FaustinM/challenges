import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace('\n', ''))

stack = []
for k in range(0, 9):
#for k in range(0, 3):
    s = []
    for i in range(7, -1, -1):
        if (lines[i][4*k+1] != ' '):
            s.append(lines[i][4*k+1])
    stack.append(s)
print(stack)

#for i in range(5, 9):
for i in range(10, 512):
    splited = lines[i].split(' ')
    print(stack[int(splited[3])-1], splited)
    stack[int(splited[5])-1] = stack[int(splited[5])-1] + stack[int(splited[3])-1][-int(splited[1]):]
    for k in range(int(splited[1])):
        if (len(stack[int(splited[3])-1]) > 0):
            stack[int(splited[3])-1].pop()
            
    
    print("-",stack[int(splited[3])-1])

for s in stack:
    print(s[-1], end='')