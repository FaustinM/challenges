import sys, typing, re, math

lines = []
for line in sys.stdin:
    lines.append(list(map(int, re.findall(r"-?\d+", line))))

sensors = []
beacons = []
for line in lines:
    d = abs(line[0]-line[2])+abs(line[1]-line[3])
    sensors.append((line[0], line[1], d))
    beacons.append((line[2], line[3]))

y = 2000000

count = 0
t = 0

max_x = max(max(beacons, key=lambda x: x[0])[0], max(sensors, key=lambda x: x[0])[0])
min_x = min(min(beacons, key=lambda x: x[0])[0], min(sensors, key=lambda x: x[0])[0])

print(max_x, min_x)
l = []
for y in range(0, 4000000):
    for i in range(0, 4000000):
        t = t + 1
        all_in = True
        for s in sensors:
            if abs(s[0]-i)+abs(s[1]-y) <= s[2]:
                all_in = False
                break

        if all_in and (i, y) not in beacons:
            print((i, y))
            break

def display(pos, calc=[]):
    min_h = pos[0][0]
    max_h = pos[0][0]
    min_w = pos[0][1]
    max_w = pos[0][1]
    for p in pos:
        if p[0] < min_h:
            min_h = p[0]
        if p[0] > max_h:
            max_h = p[0]
        if p[1] < min_w:
            min_w = p[1]
        if p[1] > max_w:
            max_w = p[1]
    
    table = [[ "." for i in range(max_w-min_w+1)] for j in range(max_h-min_h+1)]
    for i in range(len(pos)):
        table[pos[i][0]-min_h][pos[i][1]-min_w] = "#"

    for i in range(len(calc)):
        table[calc[i][0]-min_h][calc[i][1]-min_w] = "o"
    
    for row in table:
        print(*row)

# display(list(map(lambda d: list(reversed((d[0], d[1]))), beacons))+list(map(lambda d: list(reversed(d)), sensors)), l)
print(count, l)