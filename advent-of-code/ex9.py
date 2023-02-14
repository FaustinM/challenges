import sys, math

lines = []
for line in sys.stdin:
    lines.append(line)

pos = []


ropes = [[0, 0] for i in range(10)]
old_distance = [[0, 0] for i in range(10)]
for line in lines:
    data = line.split(" ")
    for i in range(int(data[1])):
        old_distance[0] = ropes[0][:]
        if (data[0]=="R"):
            ropes[0][1] = ropes[0][1] + 1
        if (data[0]=="L"):
            ropes[0][1] = ropes[0][1] - 1
        if (data[0]=="U"):
            ropes[0][0] = ropes[0][0] - 1
        if (data[0]=="D"):
            ropes[0][0] = ropes[0][0] + 1
        #print(math.dist(h_p, t_p), h_p)
        """
        for j in range(len(ropes)-1):
            dy = ropes[j][0] - ropes[j+1][0]
            dx = ropes[j][1] - ropes[j+1][1]
            if abs(dy) > 1:
                if dy < 0:
                    dy = dy+1
                else:
                    dy = dy-1
                ropes[j+1][0]=ropes[j+1][0]+dy

            if abs(dx) > 1:
                if dx < 0:
                    dx = dx+1
                else:
                    dx = dx-1
                ropes[j+1][1]=ropes[j+1][1]+dx

            if j+1 == len(ropes)-1:
                print(dy, dx)
                print(ropes[j+1])
                pos.append((ropes[j+1][0], ropes[j+1][1]))
            """
        for j in range(len(ropes)-1):
            d = math.dist(ropes[j], ropes[j+1])
            if d >= 2:
                dy = ropes[j][0] - ropes[j+1][0]
                dx = ropes[j][1] - ropes[j+1][1]
                if abs(dy) > 1:
                    if dy < 0:
                        dy = dy+1
                    else:
                        dy = dy-1
                ropes[j+1][0]=ropes[j+1][0]+dy
                if abs(dx) > 1:
                    if dx < 0:
                        dx = dx+1
                    else:
                        dx = dx-1
                ropes[j+1][1]=ropes[j+1][1]+dx
                
                if j+1 == len(ropes)-1:
                    print(dy, dx)
                    print(ropes[j+1])
                    pos.append((ropes[j+1][0], ropes[j+1][1]))



def display(pos):
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
    
    table[-min_h][-min_w] = "s"
    for row in table:
        print(*row)

# display([(0, 0), (10, 10), (5, 5), (5, 0), (0, 5), (10, 0), (0, 10), (5, 10), (10, 5)])
display(pos)
print(set(pos), len(set(pos))+1)