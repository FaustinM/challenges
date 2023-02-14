import sys
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

lines = []
for line in sys.stdin:
    lines.append(list(map(lambda d: int(d), line.strip().split(','))))

face = {}

for line in lines:
    for x in (0, -1):
        b_point = (line[0]+x, line[1], line[2]) # x y z
        s_point = (line[0]+x, line[1]-1, line[2]-1)
        if (b_point, s_point) in face:
            face[(b_point, s_point)] = face[(b_point, s_point)]+1
        else:
            face[(b_point, s_point)] = 1

    for y in (0, -1):
        b_point = (line[0], line[1]+y, line[2]) # x y z
        s_point = (line[0]-1, line[1]+y, line[2]-1)
        if (b_point, s_point) in face:
            face[(b_point, s_point)] = face[(b_point, s_point)]+1
        else:
            face[(b_point, s_point)] = 1

    for z in (0, -1):
        b_point = (line[0], line[1], line[2]+z) # x y z
        s_point = (line[0]-1, line[1]-1, line[2]+z)
        if (b_point, s_point) in face:
            face[(b_point, s_point)] = face[(b_point, s_point)]+1
        else:
            face[(b_point, s_point)] = 1

count = 0
min_x = {}
max_x = {}
min_y = {}
max_y = {}
min_z = {}
max_z = {}

for f in face:
    # z locked
    to_check = tuple(map(lambda x, y: (x + y)/2, f[0], f[1]))
    if to_check[:-1] not in min_z:
        min_z[to_check[:-1]] = to_check[-1]
    elif min_z[to_check[:-1]] > to_check[-1]:
        min_z[to_check[:-1]] = to_check[-1]

    if to_check[:-1] not in max_z:
        max_z[to_check[:-1]] = to_check[-1]
    elif max_z[to_check[:-1]] < to_check[-1]:
        max_z[to_check[:-1]] = to_check[-1]

    # x locked
    if to_check[1:] not in min_x:
        min_x[to_check[1:]] = to_check[0]
    elif min_x[to_check[1:]] > to_check[0]:
        min_x[to_check[1:]] = to_check[0]

    if to_check[1:] not in max_x:
        max_x[to_check[1:]] = to_check[0]
    elif max_x[to_check[1:]] < to_check[0]:
        max_x[to_check[1:]] = to_check[0]

    # y locked
    if (to_check[0], to_check[-1]) not in min_y:
        min_y[(to_check[0], to_check[-1])] = to_check[1]
    elif min_y[(to_check[0], to_check[-1])] > to_check[1]:
        min_y[(to_check[0], to_check[-1])] = to_check[1]

    if (to_check[0], to_check[-1]) not in max_y:
        max_y[(to_check[0], to_check[-1])] = to_check[1]
    elif max_y[(to_check[0], to_check[-1])] < to_check[1]:
        max_y[(to_check[0], to_check[-1])] = to_check[1]

def point_inside(x, y, z):
    return x == min_x[(y, z)] or x == max_x[(y, z)] or y == min_y[(x, z)] or y == max_y[(x, z)] or z == min_z[(x, y)] or z == max_z[(x, y)]

count = 0
for f in face:
    if face[f] == 1 and point_inside(*tuple(map(lambda x, y: (x + y)/2, f[0], f[1]))):
        count = count + 1
        ax.plot([f[0][0], f[1][0]],[f[0][1], f[1][1]],[f[0][2], f[1][2]], color='blue')
    elif face[f] == 1:
        ax.plot([f[0][0], f[1][0]],[f[0][1], f[1][1]],[f[0][2], f[1][2]], color='red')


print(count)
plt.show()