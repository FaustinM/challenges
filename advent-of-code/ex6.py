import sys

lines = []
for line in sys.stdin:
    lines.append(line)

for i_char in range(13, len(lines[0])):
    liste = set([lines[0][i_char-13], lines[0][i_char-12], lines[0][i_char-11], lines[0][i_char-10], lines[0][i_char-9], lines[0][i_char-8], lines[0][i_char-7], lines[0][i_char-6], lines[0][i_char-5], lines[0][i_char-4], lines[0][i_char-3], lines[0][i_char-2], lines[0][i_char-1], lines[0][i_char]])
    if (len(liste) == 14):
        print(i_char+1)
        break