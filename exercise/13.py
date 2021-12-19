def solve(arr: list[tuple[int, int]]) -> int:
    acc = [t[0] - t[1] for t in arr]
    start = 0
    while start < len(arr) and acc[start] < 0:
        start += 1
    if start == len(arr):
        return -1

    s = acc[start]
    end = start + 1
    while start != end:
        if start == len(arr):
            return -1

        if end == len(arr):
            end = 0

        s += acc[end]
        if s < 0:
            if end < start:
                return -1
            start = end + 1
            while acc[start] < 0 and start < len(arr):
                start += 1
            if start == len(arr):
                return -1

            s = acc[start]
        end += 1
    return start


# data = [(4, 6), (6, 5), (7, 3), (0, 6), (10, 2), (0, 1)]
data = [(2, 4), (7, 9), (4, 6), (6, 9)]
print(solve(data))
