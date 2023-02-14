import sys,functools 
sys.setrecursionlimit(10000)

lines = []
for line in sys.stdin:
    lines.append(eval(line.strip() or "None"))

def recursif(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else -1 if left > right else 0
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

        for i in range(len(left)):
            if i >= len(right):
                return -1

            v = recursif(left[i], right[i])
            if v == 1:
                return 1
            elif v == -1:
                return -1
    return 1 if len(left) < len(right) else -1 if len(left) > len(right) else 0
    
i = 0
s = 0
for i_line in range(0, len(lines), 3):
    i = i + 1
    if (recursif(lines[i_line], lines[i_line+1]) == 1):
        s = s + i
print(s)

lines.append([[2]])
lines.append([[6]])
packets = sorted(list(filter(lambda x: x !=None, lines)), key=functools.cmp_to_key(recursif))
packets.reverse()
for i in packets:
    print(i)
print((packets.index([[2]])+1)*(packets.index([[6]])+1))