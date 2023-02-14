import sys, math

lines = []
for line in sys.stdin:
    lines.append(line.strip())

monkeys = [None for i in range(8)]
c_key = None
s_v = 1
for line in lines:
    if line.startswith("Monkey "):
        c_key = int(line.replace("Monkey ", "").replace(":", ""))
        monkeys[c_key] = {"items" : [], "count": 0}
    if (line.startswith("Starting items: ")):
        data = line.replace("Starting items: ", "").split(", ")
        for i in range(len(data)):
            data[i] = int(data[i])
        monkeys[c_key]["items"] = data
    if (line.startswith("Operation: ")):
        data = line.replace("Operation: new = ", "")
        if '*' in data:
            data = data.split('*')
            monkeys[c_key]["operation"] = ('*', data[1])
        if '+' in data:
            data = data.split('+')
            monkeys[c_key]["operation"] = ('+', data[1])
    if (line.startswith("Test: ")):
        monkeys[c_key]["test"] = int(line.split(" ")[-1])
        s_v = s_v * monkeys[c_key]["test"]
    if (line.startswith("If true: ")):
        monkeys[c_key]["test_true"] = int(line.split(" ")[-1])
    if (line.startswith("If false: ")):
        monkeys[c_key]["test_false"] = int(line.split(" ")[-1])

print(s_v)
for i in range(10000):
    for m in monkeys:
        if m != None:
            i_it = 0
            while len(m["items"]) > 0:
                m["count"] += 1
                if m["operation"][0] == '*':
                    if m["operation"][1] == ' old':
                        m["items"][i_it] *=  m["items"][i_it]
                    else:
                        m["items"][i_it] *=  int(m["operation"][1])
                else:
                    m["items"][i_it] += int(m["operation"][1])


                m["items"][i_it] = m["items"][i_it] % s_v

                if m["items"][i_it] % m["test"] == 0:
                    monkeys[m["test_true"]]["items"].append(m["items"].pop(i_it))
                else:
                    monkeys[m["test_false"]]["items"].append(m["items"].pop(i_it))

for m in monkeys:
    if m !=None:
        print(m["count"])
