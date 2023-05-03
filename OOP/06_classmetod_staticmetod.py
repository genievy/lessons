"""
@classmethod >>> определяют методы классов, имеющие доступ только к методам и атрибутам класса, но не экземпляра
@staticmetod >>> не имеют доступ ни к атрибутам/медодам класса, ни к атрибутам/медодам класса экземрляра.
                Т. е. создается некая независимая ф-ция, объявленная внутри класса. Обычно длч удобства
"""



class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  # if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):  # просто сервисная вычислительная ф-ция внутри класса. Можно вызывать как вутри, так и снаружи.
        return x*x + y*y


v = Vector(2, 3)
print(v.norm2(5, 6))
print(Vector.validate(5))
print(v.get_coords())
