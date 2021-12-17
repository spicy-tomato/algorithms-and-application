def hash_table_linear(arr: [int], n) -> [int]:
    res = [None for _ in range(n)]
    for num in arr:
        i = 0
        m = num % n
        while res[m] is not None:
            i += 1
            m = (m + i) % n
        res[m] = num
    return res


def run():
    arr = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
    print(hash_table_linear(arr, 10))


run()
