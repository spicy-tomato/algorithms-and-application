def hash_table_quadratic(arr: [int], n) -> [int]:
    res = [[] for _ in range(n)]
    for num in arr:
        res[num % n].append(num)
    return res


def run():
    arr = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
    print(hash_table_quadratic(arr, 10))


run()
