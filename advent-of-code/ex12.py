import sys
sys.setrecursionlimit(10000)
lines = []
for line in sys.stdin:
    lines.append(line.strip())

pos_t = {}

def r(v):
    mini = 1000
    i_mini = -1
    for i in range(len(v)):
        if mini > v[i][0] and v[i][0] < 1000:
            mini = v[i][0]
            i_mini = i
    return (1+v[i_mini][0], v[i_mini][1])

"""
def route(x, y, f):
    global pos_t
    global c
    if lines[y][x] == '{':
        print("-- F --")
        display(f)
        print(len(f), f)
        print("------")
        return (1, f)
    
    #if (y, x) in c:
    #    return c[(y, x)]
    
    min_r = []

    f.append((y, x))
    for t in pos_t[(y, x)]:
        if not t in f:
            min_r.append(route(t[1], t[0], f))
    if len(min_r) > 0:
        c[(y, x)] = r(min_r)
    else:
        c[(y, x)] = (1000, [])

    if x == 1 and y == 4:
        print(c[(y, x)])
    return c[(y, x)]

c = {}
min_f = 2065
visited = []
def route(y, x, f=[]):
    global pos_t, min_f, visited
    if len(f) > min_f:
        return None

    if lines[y][x] == '{':
        print(min_f)
        if min_f > len(f): min_f = len(f)
        return f

    v = None
    for p in pos_t[(y, x)]:
        if not p in f and not p in visited:
            visited.append((y, x))
            val = route(p[0], p[1], f+[(y, x)])
            if(val and (not v or len(v) > len(val))):
                v = val
    return v
"""
def route(y, x,dict):
    global lines
    D = {v:float('inf') for v in dict}
    D[(y, x)] = 0
    candidates = [(y, x)]
    visited = []
    path = {}
    while (len(candidates) > 0):
        n = candidates.pop(0)
        visited.append(visited)
        for neight in dict[(n[0], n[1])]:
            if neight not in visited:
                old_cost = D[neight]
                new_cost = D[n] + 1
                if new_cost < old_cost:
                    candidates.append(neight)
                    D[neight] = new_cost
    return D

for y in range(len(lines)):
    for x in range (len(lines[0])):
        line = lines[y][x]
        targets = []

        if y+1 < len(lines) and (ord(lines[y+1][x]) - ord(line) <= 1):
            targets.append((y+1, x))
        if y-1 >= 0 and (ord(lines[y-1][x]) - ord(line) <= 1):
            targets.append((y-1, x))
        if x+1 < len(lines[0]) and ord(lines[y][x+1]) - ord(line) <= 1:
            targets.append((y, x+1))
        if x-1 >= 0 and (ord(lines[y][x-1]) - ord(line) <= 1):
            targets.append((y, x-1))

        pos_t[(y, x)] = targets

pos_t[(20,0)] = [(19, 0), (21, 0), (20, 1)]

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

#print(lines[20][135])

def invert_dict(d): 
    inverse = dict() 
    for key in d: 
        # Go through the list that is saved in the dict:
        for item in d[key]:
            # Check if in the inverted dict the key exists
            if item not in inverse: 
                # If not create a new list
                inverse[item] = [key] 
            else: 
                inverse[item].append(key) 
                
    for key in inverse:
        for i in inverse[key]:
            if i not in inverse:
                inverse[key].remove(i)
                
    return inverse

pos_t_reversed = invert_dict(pos_t)

#d = route(2, 5, pos_t_reversed)
# print(pos_t_reversed)
d = route(20, 135, pos_t_reversed)
d_s = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
for i in d_s:
    if lines[i[0]][i[1]] == "a":
        print(i, d_s[i])
        break
#display(visited)
#display(route(0, 0))
#print(len(route(0, 0)))
#print(pos_t[(4, 3)])
# print(pos_t[1, 7], pos_t[4, 1])