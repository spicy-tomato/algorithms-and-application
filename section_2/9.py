def sum_of_num(n: int) -> int:
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


def my_sort(arr: [int]) -> [int]:
    b = [(k, sum_of_num(k)) for i, k in enumerate(arr)]
    b = sorted(b, key=lambda x: (x[1], x[0]))
    return [x[0] for x in b]


a = [13, 20, 7, 4]
print(my_sort(a))
