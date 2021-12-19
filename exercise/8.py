a = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]
tanxuat = []
caonhat = []
cuoicung = []


def fillmang():
    for i in range(10):
        tanxuat.append(0)
        cuoicung.append(0)


def timtanxuat():
    fillmang()
    tmp = 0
    for i in a:
        tanxuat[i] += 1
    tmp = max(tanxuat)
    for i in range(len(tanxuat)):
        if tanxuat[i] == tmp:
            caonhat.append(i)


def countingsort():
    for i in range(1, len(a)):
        tanxuat[i] += tanxuat[i - 1]
    for i in range(len(a)):
        cuoicung[tanxuat[a[i]] - 1] = a[i]
        tanxuat[a[i]] -= 1


def run():
    timtanxuat()
    countingsort()
    print(cuoicung)
    print("mốt", caonhat)
    if len(cuoicung) % 2 == 0:
        print("Phan tu trung vi", (cuoicung[0] + cuoicung[len(cuoicung) - 1]) / 2)
    else:
        print("Phan tu trung vi", cuoicung[int(len(cuoicung) / 2)])


run()
