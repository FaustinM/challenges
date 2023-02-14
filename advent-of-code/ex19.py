import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.strip()))

final_lines = lines[:]

def get_real_index(lst, i):
    return i % len(lst)

for i in range(len(lines)):
    final_lines.insert(get_real_index(final_lines, i+lines[i]), lines.pop(i))

print(final_lines)