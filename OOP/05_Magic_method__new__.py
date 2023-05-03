""" __new__ вызывается непосредственно перед сщзданием объекта класса
    __init__ вызывается непосредственно после создания объекта класса
"""


class Point:

    __instance = None

    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для: ", str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("вызов __init__ для: ", str(self))
        self.x = x
        self.Y = y


pt = Point(1, 2)
print(pt.__dict__)


""" 
    Pattern  Singleton 
    Предполагается, что в программе в данный момент времени должен существовать только одинэкземпляр этого класса
    Определим класс, и в котором классе создадим условие, которое перед созданием экземпляра класса 
    будет определять, существует ли уже в данный момен экземпляр класса:
"""


class DataBase:

    """Определим внутреннюю переменную, которая принимает значение по умолчанию None"""
    __instance = None

    """Определим метод __new__, который вызывается перед созданием объекта класса, 
     но таким образом, что он будет присваивать  переменной __instance значение адреса объекта,
     или возвращать существующий адрес, если __instance не None.
    """
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print(f"Закрытие БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"Запись в БД: {data}")


db = DataBase('root', '123', 80)
db2 = DataBase('root2', '1234455', 3088)

db.connect()
db2.connect()

print(str(db))
print(str(db2))
print(id(db), id(db2))


"""
Вывод:
<__main__.DataBase object at 0x000000000234D7F0>
<__main__.DataBase object at 0x000000000234D7F0>
37017584 37017584

"""

"""Но если мы вызовем метод .connect() для этих двух объектов:"""
db.connect()
db2.connect()

""" То увидим, что он вызывается для объекта, созданного с аргументами переданными во второй раз:
Вывод:
Соединение с БД: root2, 1234455, 3088
Соединение с БД: root2, 1234455, 3088

Чтобы это поправить, используется магический метод __call__
Но об этом далее!
"""

