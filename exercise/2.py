def hash_table_linear(arr: [int], n) -> [int]:
    res = [None for _ in range(n)]
    for num in arr:
        m = num % n
        while m < n and res[m] is not None:
            m += 1
        if m >= n:
            m = 0
            while m < n and res[m] is not None:
                m += 1
        res[m] = num
    return res


def run():
    arr = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
    print(hash_table_linear(arr, 10))


run()
