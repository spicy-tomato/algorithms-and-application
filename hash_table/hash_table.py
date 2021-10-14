class HashTable:
    def __init__(self, hash_func, bucket_size: int):
        self.hash_func = hash_func
        self.bucket_size = bucket_size
        self.buckets: list[tuple] = [(None, None) for _ in range(bucket_size)]

    def insert(self, key: str, value: str) -> None:
        hash_value: int = self.hash_func(key, self.bucket_size)

        while self.buckets[hash_value][0] != None:
            hash_value = (hash_value + 1) % self.bucket_size
        self.buckets[hash_value] = (key, value)

    def get(self, key):
        hash_value: int = self.hash_func(key, self.bucket_size)

        while self.buckets[hash_value][0] != None and self.buckets[hash_value][0] != key:
            hash_value = (hash_value + 1) % self.bucket_size
        return self.buckets[hash_value][1]

    def size(self):
        return sum([len(i) for i in self.buckets])


def hash_function(word: str, bucket_size: int) -> int:
    _sum = sum([ord(c) for c in word])
    return _sum % bucket_size


ht = HashTable(hash_function, 23)

ht.insert('a', 'a')
ht.insert('b', 'b')
ht.insert('c', 'c')
ht.insert('d', 'd')
ht.insert('e', 'e')
ht.insert('f', 'f')
ht.insert('g', 'g')
ht.insert('h', 'h')
ht.insert('i', 'i')
ht.insert('k', 'k')
ht.insert('cat', 'mèo')
ht.insert('dog', 'chó')
ht.insert('house', 'nhà')
ht.insert('lag', 'giật')
ht.insert('actor', 'diễn viên')
ht.insert('lost', 'mất')
ht.insert('a', 'a')


print('actor:', ht.get('actor'))

print('dog:', ht.get('dog'))
print('house:', ht.get('house'))
print('lag:', ht.get('lag'))
print('actor:', ht.get('actor'))
print('lost:', ht.get('lost'))
