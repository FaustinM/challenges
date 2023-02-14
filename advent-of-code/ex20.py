import sys, ctypes

lines = []
for line in sys.stdin:
    lines.append(int(line.strip()))

final_lines = list(map(lambda d: id(d), lines))

def get_real_index(lst, i):
    return i % (len(lst))

for i in range(len(lines)):
    final_index = final_lines.index(id(lines[i]))
    popped_line = final_lines.pop(final_index)
    real_index = get_real_index(final_lines, final_index+lines[i])
    final_lines.insert(real_index, popped_line)
    #print(list(map(lambda d: ctypes.cast(d, ctypes.py_object).value, final_lines)))

debind_list = list(map(lambda d: ctypes.cast(d, ctypes.py_object).value, final_lines))
print(sum([
    debind_list[get_real_index(debind_list, debind_list.index(0)+1000)], 
    debind_list[get_real_index(debind_list, debind_list.index(0)+2000)],
    debind_list[get_real_index(debind_list, debind_list.index(0)+3000)]
    ]))