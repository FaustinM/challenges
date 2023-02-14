import sys

char = []

lines = []
#for line in sys.stdin:
#    lines.append(line)

for line in lines:
    fp = line[:int(len(line)/2)]
    sp = line[int(len(line)/2):]
    print(len(line), fp, sp)
    line_score = []
    for c in fp:
        if c in sp:
            if not c in line_score:
                line_score.append(c)
    char = char + line_score

sum = 0
for c in char:
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        sum+=(ord(c)-ord('a'))+1
    else:
        sum+=(ord(c)-ord('A'))+27
print(sum)