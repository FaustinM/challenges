import sys, math

lines = []
data = {}
for line in sys.stdin:
    line_split = line.strip().split(':')
    if (line_split[1][1:].isdigit()):
        data[line_split[0]] = { "value": int(line_split[1]) }
    else:
        request = line_split[1].split(' ')[1:]
        data[line_split[0]] = { "need": (request[0], request[2]), "oppr": request[1]}

def compute_value(oppr, values):
    if oppr == "*":
        return math.prod(values)
    elif oppr == "+":
        return sum(values)
    elif oppr == "/":
        return values[0]/values[1]
    elif oppr == "-":
        return values[0]-values[1]
    elif oppr == "=":
        return values[0]==values[1]
    else:
        return 0

def get_value(id):
    global data
    if 'value' in data[id]:
        return data[id]['value']

    values = []
    for n in data[id]["need"]:
        values.append(get_value(n))
    c_value = compute_value(data[id]['oppr'], values)
    if id == 'root':
        print(values)
    data[id]['value'] = c_value
    return c_value

print(get_value('root'), len(str(int(get_value('root')))))