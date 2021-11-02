"""
Bài 7. Cho một ma trận trong đó mỗi ô trong ma trận có thể có các giá trị 0, 1 hoặc 2 có
nghĩa sau:
• 0: Là một ô trống.
• 1: Là một quả cam tươi.
• 2: Là một quả cam bị hỏng.
Chúng ta phải xác định thời gian tối thiểu mà tất cả các quả cam bị hỏng. Một quả cam hỏng
ở chỉ số [i, j] có thể làm hỏng quả cam tươi khác ở các chỉ số [i-1, j], [i + 1, j], [i, j-1], [i, j + 1]
(lên , xuống, trái và phải). Nếu không thể bị hỏng tất cả quả cam thì trả về -1.
Ví dụ:
• Với matrix = [
    [2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]].
Thì đầu ra có dạng rotOrange(matrix) = 2
• Với matrix = [
    [2, 1, 0, 2, 1],
    [0, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]].
Thì đầu ra có dạng rotOrange(matrix) = -1
"""


def rot_orange(mat: [[int]]):
    good = 0
    result = 0
    rows = len(mat)
    cols = len(mat[0])
    queue = []

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                good += 1
            elif mat[i][j] == 2:
                queue.append((i, j, 0))

    while len(queue) > 0:
        row, col, count = queue.pop(0)
        if row > 0 and mat[row - 1][col] == 1:
            mat[row - 1][col] = 2
            queue.append((row - 1, col, count + 1))
            good -= 1
        if row < rows - 1 and mat[row + 1][col] == 1:
            mat[row + 1][col] = 2
            queue.append((row + 1, col, count + 1))
            good -= 1
        if col > 0 and mat[row][col - 1] == 1:
            mat[row][col - 1] = 2
            queue.append((row, col - 1, count + 1))
            good -= 1
        if col < cols - 1 and mat[row][col + 1] == 1:
            mat[row][col + 1] = 2
            queue.append((row, col + 1, count + 1))
            good -= 1
        if good == 0:
            return count + 1

    return -1


mat1 = [
    [2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]
]

mat2 = [
    [2, 1, 0, 2, 1],
    [0, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]
]

print(rot_orange(mat1))
print(rot_orange(mat2))
