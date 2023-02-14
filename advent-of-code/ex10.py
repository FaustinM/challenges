import sys

reg = 1
cycle = 0

lines = []
for line in sys.stdin:
    lines.append(line)


ss = []
def control_signal(reg, cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(reg, cycle)
        ss.append(reg*cycle)

screen_s = ""
def draw_screen():
    global screen_s
    pos = len(screen_s)%40+1
    if pos == reg or pos == reg+1 or pos == reg+2:
        screen_s = screen_s + "#"
    else:
        screen_s = screen_s + " "
    

while (len(lines) > 0):
    data = lines.pop(0).split(" ")
    cycle = cycle + 1
    control_signal(reg, cycle)
    draw_screen()
    if data[0] == "noop":
        pass
    elif data[0]== "addx":
        cycle = cycle + 1
        control_signal(reg, cycle)
        draw_screen()
        reg = reg + int(data[1])

print("---")
for j in [screen_s[i:i+40] for i in range(0, len(screen_s), 40)]:
    print(j)
