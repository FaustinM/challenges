import sys

lines = []
score = 0
same = { "A": "X", "B": "Y", "C": "Z"}
win = { "A": "Y", "B": "Z", "C": "X"}
loss = { "A": "Z", "B": "X", "C": "Y"}

win_target = {"X": "C", "Y": "A", "Z": "B"}
for line in sys.stdin:
    scores_both = line.strip().split(' ')

    if scores_both[1]=='X':
        scores_both[1] = loss[scores_both[0]]
    elif scores_both[1]=='Y':
        scores_both[1] = same[scores_both[0]]
    elif scores_both[1]=='Z':
        scores_both[1] = win[scores_both[0]]

    if scores_both[1]=='X':
        score += 1
    elif scores_both[1]=='Y':
        score += 2
    elif scores_both[1]=='Z':
        score += 3

    if scores_both[1] == same[scores_both[0]]:
        score += 3
    elif win_target[scores_both[1]] == scores_both[0]:
        score += 6
    
print(score)
        