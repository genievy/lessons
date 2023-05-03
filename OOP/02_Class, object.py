# https://www.youtube.com/watch?v=P4CNNo8jWj4&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=2

class Point:  # имя класса с большой буквы и передает смысл значения класса
    "Класс для представления координат на плоскости"
    color = 'red'  # переменные внутри класса - атрибуты(свойства)
    circle = 2     # эти атрибуты находятся в пространстве имен класса Point


"""
>>> Point.color = 'black'
>>> Point.__dict__

>>> mappingproxy({'__module__': '__main__',
              'color': 'black',
              'circle': 2,
              '__dict__': <attribute '__dict__' of 'Point' objects>,
              '__weakref__': <attribute '__weakref__' of 'Point' objects>,
              '__doc__': None})

добавление атрибута
setattr(b, 'prop', 'square')
setattr(Point, 'prop', a.prop)

получить атрибут
getattr(Point, 'color')
getattr(Point, 'mass', False)

удалить атрибут
delattr(a, 'prop')
del Point.prop

проверить наличие атриута
hasattr(Point, 'color')

>>> Point.__doc__    --> содержит строку с оеписанием класса
"Класс для представления координат на плоскости"

.__dict__    --> содержит набор атрибутов экземпляра класса

"""