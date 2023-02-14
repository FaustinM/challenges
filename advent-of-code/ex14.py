import sys, time

sand = (0, 500)

lines = []
for line in sys.stdin:
    lines.append(line.strip())

cave = [(0, 500)]

# (y, x)
for line in lines:
    data = line.split(' -> ')
    for d in range(0, len(data)-1):
        coords_1 = list(reversed(list(map(lambda i: int(i), data[d].split(',')))))
        coords_2 = list(reversed(list(map(lambda i: int(i), data[d+1].split(',')))))

        to_change = [coords_1[0], coords_2[0]]
        first = True

        if coords_1[0] == coords_2[0]:
            to_change = [coords_1[1], coords_2[1]]
            first = False
        
        cave.append(tuple(coords_1))

        for i in range(min(to_change), max(to_change)):
            if (first):
                cave.append((i, coords_1[1]))
            else:
                cave.append((coords_1[0], i))
    
    cave.append(tuple(reversed(list(map(lambda i: int(i), data[-1].split(','))))))

max_y = max(cave, key=lambda c:c[0])[0]+2
for i in range(min(cave, key=lambda c: c[1])[1]-300, max(cave, key=lambda c: c[1])[1]+300):
    cave.append((max_y, i))

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

    table[sand[0]-min_h][sand[1]-min_w] = "S"
    
    for row in table:
        print(*row)

sands = []
possible = True


max_x_s = max(cave, key=lambda c:c[1])[1]
max_y_s = max(cave, key=lambda c:c[0])[0]
sands_data = [[False for i in range(max_x_s+2)] for j in range(max_y_s+2)]
while(possible):
    sands.append([0, 500])

    whole_blocked = True
    s = sands[-1]
    while (whole_blocked):
        sands_data[s[0]][s[1]] = False
        whole_blocked = False
        if (s[0]+1, s[1]) not in cave and not sands_data[s[0]+1][s[1]]:
            s[0] = s[0]+1
            whole_blocked = True
        else:
            if (s[0]+1, s[1]-1) not in cave and not sands_data[s[0]+1][s[1]-1]:
                s[1] = s[1]-1
                s[0] = s[0]+1
                whole_blocked = True
            else:
                if (s[0]+1, s[1]+1) not in cave and not sands_data[s[0]+1][s[1]+1]:
                    s[1] = s[1]+1
                    s[0] = s[0]+1
                    whole_blocked = True
        sands_data[s[0]][s[1]] = True
    if sands[-1] == [0, 500]:
        possible = False

    if len(sands)%10==0:
        print(len(sands)) 
        display(cave, sands)
print(len(sands)) 
display(cave, sands)