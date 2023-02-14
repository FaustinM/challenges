import sys

lines = []
for line in sys.stdin:
    lines.append(line)

count = 0
for line in lines:
    a = line.split(",")
    f = a[0].split("-")
    s = a[1].split("-")
    f[1] = int(f[1])
    f[0] = int(f[0])
    s[1] = int(s[1])
    s[0] = int(s[0])
    f_s = set()
    s_s = set()
    for n in range(f[0], f[1]+1):
        f_s.add(n)
    for n in range(s[0], s[1]+1):
        s_s.add(n)

    inter = f_s.intersection(s_s)
    if (len(inter) > 0):
        count = count +1
    
print(count)