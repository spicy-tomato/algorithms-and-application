a = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]
freq = []
mode = []
last = []


def fill_array():
    for i in range(10):
        freq.append(0)
        last.append(0)


def find_freq():
    fill_array()
    for i in a:
        freq[i] += 1
    tmp = max(freq)
    for i in range(len(freq)):
        if freq[i] == tmp:
            mode.append(i)


def counting_sort():
    for i in range(1, len(a)):
        freq[i] += freq[i - 1]
    for i in range(len(a)):
        last[freq[a[i]] - 1] = a[i]
        freq[a[i]] -= 1


def run():
    find_freq()
    counting_sort()
    print(last)
    print("Mot", mode)
    if len(last) % 2 == 0:
        print("Trung vi", (last[0] + last[len(last) - 1]) / 2)
    else:
        print("Trung vi", last[int(len(last) / 2)])


run()
