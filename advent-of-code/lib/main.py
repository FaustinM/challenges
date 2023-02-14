import typing

# Math
def min_max(l):
    return min(l), max(l)

def max_minus_min(l):
    return max(l) - min(l)

# Regex
def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!
def positive_ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d+", s))  # thanks mserrano!