import sys

currentValue = 0

maxV = []
for line in sys.stdin:
    if (line.strip() == ""):
        maxV.append(currentValue)
        currentValue = 0
    else:
        currentValue = currentValue + int(line.strip())

maxV.sort()
print(maxV[-3:])