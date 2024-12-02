from pprint import pp


def load(fpath: str) -> tuple[list[int], list[int]]:
    """
    Loads the 2 lists, left and right column. Sorts before returning.

    Example format:
    ```
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    ```
    """

    left = []
    right = []
    with open(fpath) as f:
        while line := f.readline():
            value1, value2 = line.split(" " * 3)
            left.append(int(value1))
            right.append(int(value2))

    left.sort()
    right.sort()
    return left, right


def distance_between(left: int, right: int) -> int:
    return abs(left - right)


if __name__ == "__main__":
    # left, right = load("example.txt")
    left, right = load("data.txt")
    distance = []
    similarity = []
    for lv, rv in zip(left, right):
        similarity.append(lv * right.count(lv))
        distance.append(distance_between(lv, rv))
    pp(sum(distance))
    pp(sum(similarity))