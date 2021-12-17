def get_sum(s: str) -> int:
    return sum(ord(c) for c in s)


def hash_table_linear(arr: [tuple[str, str]], n) -> [int]:
    res = [None for _ in range(n)]
    for pair in arr:
        i = 0
        m = get_sum(pair[0]) % n
        while res[m] is not None:
            i += 1
            m = (m + i) % n
        res[m] = pair
    return res


def run():
    arr = [
        ('hello', 'xin chao'),
        ('good', 'tot'),
        ('sad', 'buon'),
        ('dog', 'cho'),
        ('cat', 'meo'),
        ('pig', 'heo'),
        ('car', 'o to')
    ]

    print(hash_table_linear(arr, 10))


run()
