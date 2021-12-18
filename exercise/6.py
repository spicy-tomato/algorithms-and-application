def max_multiply(arr: list[int], k) -> list[int]:
    res: list[int] = []
    q: list[int] = []
    s = 1

    for i in range(k):
        s *= arr[i]
        q.append(arr[i])
        if i == k - 1:
            res.append(s)
        else:
            res.append(-1)

    q.sort()

    for i in range(k, len(arr)):
        if arr[i] > q[0]:
            try:
                q.index(arr[i])
            except ValueError:
                old = q.pop(0)
                q.append(arr[i])
                q.sort()
                s = int(s/old) * arr[i]
        res.append(s)
    return res


def run():
    arr = [1, 2, 3, 3, 4, 5]
    k = 3
    print(max_multiply(arr, k))


run()
