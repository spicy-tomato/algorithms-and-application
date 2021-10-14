from binary_tree import BinaryTree
from student import Student

tree = BinaryTree()

tree.insert(2, Student('A', True, 'A_Address', '1', 8))
tree.insert(1, Student('B', True, 'B_Address', '2', 5))
tree.insert(3, Student('C', True, 'C_Address', '3', 7.5))
tree.insert(5, Student('D', True, 'D_Address', '2', 9))
tree.insert(4, Student('E', True, 'E_Address', '3', 7))
tree.insert(6, Student('F', True, 'F_Address', '1', 8))

print(tree.find_highest('avg', 5))

tree.delete(5)

print(tree.find_highest('avg', 5))
