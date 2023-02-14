import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

ls_mode = False
sum_dir = 0
path = []
tree = {}

for line in lines:
    splited_line = line.split(' ')
    if line.startswith('$'):
        if splited_line[1] == 'ls':
            ls_mode = True
        elif splited_line[1] == 'cd':
            if splited_line[2] == '..':
                path.pop()
            else:
                path.append(splited_line[2])
                if not "/".join(path) in tree:
                    tree["/".join(path)] = []
    elif ls_mode:
        if splited_line[0] == 'dir':
            tree["/".join(path)].append(("/".join(path) + '/' + splited_line[1], None))
        else:
            tree["/".join(path)].append(("/".join(path) + '/' + splited_line[1], int(splited_line[0])))


def somme(liste):
    s = 0
    for i in liste:
        if i[1] != None:
            s = s + i[1]
        else:
            s = s + somme(tree[i[0]])
    return s

m = []
l = 70000000 - 43441553
m_i = None
m_v = 0
for i in tree:
    s = somme(tree[i])
    if (l + s > 30000000):
        if not m_i or m_v > s:
            m_i = i
            m_v = s

print(m_i, m_v)