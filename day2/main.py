# ruff: noqa: E731
from pprint import pp
from typing import Any

noop = lambda *a, **b: ...

# Calls `next()` but returns none instead of throwing
def next_nothrow(obj: Any):
    try:
        return next(obj)
    except StopIteration:
        return None


def load(fpath: str) -> list[list[int]]:
    data = []
    with open(fpath) as f:
        while line := f.readline():
            a = line.split(" ")
            data.append([int(v) for v in a])
    return data


def calc(line: list[int]) -> bool:
    # two branches; either can increase or decrease from start to end of line
    first, last = line[0], line[-1]

    # calculate if distance of l, and r is at least one and at most 3
    in_range = lambda l, r: 0 < (abs(l - r)) and (abs(l - r)) < 4

    decr = lambda l, r: l > r  # left should be bigger than right
    incr = lambda l, r: l < r  # Left should be smaller than right
    cmp = incr if first < last else decr

    array = iter(line[1:])
    prev = first
    bad_value = True
    while i := next_nothrow(array):
        if i is None:
            break
        if not cmp(prev, i):
            if bad_value:
                return False
            bad_value = True

        if not in_range(prev, i):
            if bad_value:
                return False
            bad_value = True


        prev = i
        continue
        if not bad_value:
            prev = i
        else:
            # If this is hit, right is a problem number
            prev = next_nothrow(array)
    return True


if __name__ == "__main__":
    data = load("day2/data.txt")
    # data = load("day2/example.txt")

    v = []
    for row in data:
        x = calc(row)
        pp(x)
        v.append(x)

    pp(f"True: {v.count(True)}\nFalse: {v.count(False)}")
