class Student:
    def __init__(self, name: str, is_male: bool, address: str, clazz: str, avg: float):
        self.name = name
        self.is_male = is_male
        self.address = address
        self.clazz = clazz
        self.avg = avg

    def __lt__(self, other) -> bool:
        if self.avg < other.avg:
            return True
        if self.avg > other.avg:
            return False
        if self.name < other.name:
            return True
        if self.name > other.name:
            return False
        if self.clazz < other.clazz:
            return True
        if self.clazz > other.clazz:
            return False
        if self.is_male < other.is_male:
            return True
        if self.is_male > other.is_male:
            return False

    def __str__(self):
        return str.format('Tên: {} - điểm: {};', self.name, self.avg)

    def __repr__(self):
        return str.format('Tên: {} - điểm: {};', self.name, self.avg)
