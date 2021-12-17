def compare(a: int, b: int, k: int):
    ma = a % k
    mb = b % k
    if ma < mb:
        return -1
    if ma > mb:
        return 1
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def my_sort(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    res = arr.copy()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if compare(res[i], res[j], k) > 0:
                tmp = res[i]
                res[i] = res[j]
                res[j] = tmp
    return res


data = [i for i in range(108)]
K = 10
print(my_sort(data, K))
