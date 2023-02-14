import sys, re
sys.setrecursionlimit(20000)

lines = []
for line in sys.stdin:
    lines.append(line.strip())

data = {}
for line in lines:
    s = re.findall(r"[A-Z]{2}|[0-9]+", line)
    d = {"flow": int(s[1]), "next_to": s[2:], "key": s[0]}
    data[s[0]] = d

cache = {}
def meilleur_combi(point, temps=30, path=[], flow=0, opens=[]):
    c_opens = opens[:]

    if (temps, tuple(sorted(opens)), point['key']) in cache:
        return cache[(temps, tuple(sorted(opens)), point['key'])]
    
    if len(c_opens) == len(data) or temps <= 0:
        return (flow, path, c_opens)

    m = []

    for v in point['next_to']:
        #if len(path) == 0 or path[-1] != data[v]:
        m.append(meilleur_combi(data[v], temps-1, path+[point], flow, c_opens))

    if temps >= 2 and point['flow'] != 0 and point['key'] not in c_opens:
        temps = temps - 1
        flow = flow + point['flow']*temps
        for v in point['next_to']:
            #if len(path) == 0:
            m.append(meilleur_combi(data[v], temps-1, path+[point], flow, c_opens+[point['key']]))

    # if point['key']=='AA':
    #     for i in m:
    #         if i[1][1]['key'] == 'II':
    #             print(i)

    # if point['key']=='JJ' and path[-1]['key'] == 'II':
    #     print(len(m))

    cache[(temps, tuple(sorted(opens)), point['key'])] = max(m, key=lambda d: d[0], default=(0, path, c_opens))
    return cache[(temps, tuple(sorted(opens)), point['key'])]

best_data = meilleur_combi(data['AA'], 18)
print(*list(map(lambda d: d['key'], best_data[1])))

print(best_data[0], best_data[2])

def DFS(g):
    opens = []
    time = 30
    visited = {i: False for i in g}
    stack = []
    stack.append('AA')
    parents = {}

    while (len(stack)):
        s = stack[-1]
        stack.pop()

        if not visited[s]:
            print(s, stack)
            visited[s] = True
        for node in g[s]['next_to']:
            if not visited[node]:
                stack.append(node)

# DFS(data)

def timed_path_DFS(g, time=30):
    opens = []
    
    stack = []
    flow = 0
    stack.append(g)
    time = time + 1

    path = []

    while len(stack):
        time = time - 1
        s = stack[-1]
        stack.pop()
        path.append(s)

        flow_to_add = (time-1)*s['flow']

        for node in s['next_to']:
            stack.append(node['key'])
    

#timed_path_DFS(data['II'], 2)