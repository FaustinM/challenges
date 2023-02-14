import sys

lines = []
for line in sys.stdin:
    lines.append([int(i) for i in line.strip()])

"""
vi = [[False for i in range(len(l))] for l in lines]
for vx in range(len(vi)):
    for vy in range(len(vi)):
        if(vy==0 or vy==len(vi[vx])-1 or vx==0 or vx==len(vi)-1): vi[vx][vy]=True

max_t = lines[0]
for i in range(0, len(lines)):
    max_l = 0
    for j in range(0, len(lines[i])):
        if (lines[i][j] > max_l): 
            max_l = lines[i][j]
            vi[i][j] = True
        if (lines[i][j] > max_t[j]): 
            max_t[j] = lines[i][j]
            vi[i][j] = True

max_t = lines[-1]
for i in range(len(lines)-1, 0, -1):
    max_l = 0
    for j in range(0, len(lines[i])):
        if (lines[i][j] > max_l): 
            max_l = lines[i][j]
            vi[i][j] = True
        if (lines[i][j] > max_t[j]): 
            max_t[j] = lines[i][j]
            vi[i][j] = True

max_t = lines[-1]
for i in range(len(lines)-1, 0, -1):
    max_l = 0
    for j in range(len(lines[i])-1, 0, -1):
        if (lines[i][j] > max_l): 
            max_l = lines[i][j]
            vi[i][j] = True
        if (lines[i][j] > max_t[j]): 
            max_t[j] = lines[i][j]
            vi[i][j] = True

max_t = lines[0]
for i in range(0, len(lines)):
    max_l = 0
    for j in range(len(lines[i])-1, 0, -1):
        if (lines[i][j] > max_l): 
            max_l = lines[i][j]
            vi[i][j] = True
        if (lines[i][j] > max_t[j]): 
            max_t[j] = lines[i][j]
            vi[i][j] = True
"""

def value(i, j, debug=False):
    nb_t = 1
    nb_v = 0
    pres_v = lines[i][j]
    for x in range(j+1, len(lines[i])):
        if lines[i][x] < pres_v:
            nb_v = nb_v + 1
        else:
            nb_v = nb_v + 1
            break
    debug and print("r", nb_v)
    nb_t = nb_t * nb_v
    
    nb_v = 0
    pres_v = lines[i][j]
    for x in range(j-1, -1, -1):
        if lines[i][x] < pres_v:
            nb_v = nb_v + 1
        else:
            nb_v = nb_v + 1
            break
    debug and print("l", nb_v)
    nb_t = nb_t * nb_v

    nb_v = 0
    pres_v = lines[i][j]
    for x in range(i+1, len(lines)):
        if lines[x][j] < pres_v:
            nb_v = nb_v + 1
        else:
            nb_v = nb_v + 1
            break
    debug and print("b", nb_v)
    nb_t = nb_t * nb_v
    
    nb_v = 0
    pres_v = lines[i][j]
    for x in range(i-1, -1, -1):
        if lines[x][j] < pres_v:
            nb_v = nb_v + 1
        else:
            nb_v = nb_v + 1
            break
    debug and print("t", nb_v)
    nb_t = nb_t * nb_v
    return nb_t
    
max_i = None
max_v = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        v = value(i, j)
        if (v > max_v):
            max_v = v
            max_i = (i, j)


print(max_i, max_v)
value(*max_i, True)
value(1, 2, True)