import random

from heap import Heap
from priority_queue import PriorityQueue

pq = PriorityQueue()
for i in range(0, 10):
    pq.push(int(random.random() * 100))

while not pq.empty():
    print(pq.top(), end=' ')
    pq.pop()

s = 'SORTEXAMPLE'
arr = [char for char in s]
Heap.sort(arr)

print()
print(arr)
