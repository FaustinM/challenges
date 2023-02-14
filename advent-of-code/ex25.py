import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

def c_to_int(c):
    if c == '2':
        return 2
    if c == '1':
        return 1
    if c == '0':
        return 0
    if c == '-':
        return -1
    if c == '=':
        return -2

def int_to_c(c):
    if c == 2:
        return '2'
    if c == 1:
        return '1'
    if c == 0:
        return '0'
    if c == 3:
        return '='
    if c == 4:
        return '-'
    return '?'


def int_to_s(s):
    sm = ""
    while s > 0:
        m = (s % 5)
        if m == 3:
            s = (s+2)//5
        elif m == 4:
            s = (s+1)//5
        else:
            s = s//5
        sm = int_to_c(m) + sm
    print(sm)

def s_to_int(s):
    sm = 0
    for i in range(0, len(s)):
        d = (5**i) * c_to_int(s[-(i+1)])
        sm = sm+d
    return sm

s = 0
for l in lines:
    s = s + (s_to_int(l))
int_to_s(s)