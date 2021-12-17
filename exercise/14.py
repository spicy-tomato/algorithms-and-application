import sys


def solve(arr: list[int], scope: int) -> list[int]:
    max_in_scope = arr[0]
    max_index = 0
    max_left = len(arr) - scope + 1
    res = []

    for i in range(1, scope):
        if arr[i] >= max_in_scope:
            max_in_scope = arr[i]
            max_index = i

    res.append(max_in_scope)

    for i in range(1, max_left):
        right = i + scope - 1
        if i > max_index:
            if arr[right] >= max_in_scope:
                max_in_scope = arr[right]
                max_index = right
                res.append(max_in_scope)
                continue
            max_in_scope = arr[i]
            for j in range(i, i+k):
                if arr[j] >= max_in_scope:
                    max_in_scope = arr[j]
                    max_index = j
                    continue
            res.append(max_in_scope)

        if arr[right] >= max_in_scope:
            max_in_scope = arr[right]
            max_index = right
        res.append(max_in_scope)

    return res


data = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print(solve(data, k))
