def solve(arr: list[tuple[int, int]]) -> int:
    acc = [t[0] - t[1] for t in arr]
    i = 0
    while acc[i] < 0 and i < len(arr):
        i += 1
    if i == len(arr):
        return -1

    s = acc[i]
    j = i + 1
    while i != j:
        if i == len(arr):
            return -1

        if j == len(arr):
            j = 0

        s += acc[j]
        if s < 0:
            if j < i:
                return -1
            i = j + 1
            while acc[i] < 0 and i < len(arr):
                i += 1
            if i == len(arr):
                return -1

            s = acc[i]
        j += 1
    return i


data = [(4, 6), (6, 5), (7, 3), (0, 6), (10, 2), (0, 1)]
print(solve(data))
