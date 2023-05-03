

person = {'name' : 'vasya', 'sernsme' : 'pupkin', 'email' : 'abcd@mail.com'}
# print(person)

# d = dict(name = 'petr', tel = '123')
#
# name = person['name']
# print(name)
#
# # tel = person['tel']
# # print(tel)
#
# tel = person.setdefault('tel', '12345')
# print(tel)
# print()
# print(person)

# tel = person.get('tel', '123')
# print(tel)

# for item in person.keys():
#     print(item)

# d = person.keys()
# print(d)

# d = person.items()
# print(d)

# #выводит на печать все элементы в столбик
# for item in person.items():
#     # print(item)
#     for elm in item:
#         print(elm)
#
# #выводит на печать все элементы в столбик попарно "ключ: значение"
# for key, value in person.items():
#     print(key, value)

# for key, value in person.items():
#     key = value
#     print(key)
    # print(value)
#
# #выводит на печать все элементы в строку через пробел
# s = []
# for item in person.items():
#     for elm in item:
#         s.append (elm)
# print(' '.join(s))
#
# #изменяем содержание словаря метод update
# new_d = {'name':'ivan', 'tel':'1234567' }
# person.update(new_d)
# print(person)


# def a():
#     print('hello')
#     return 'hello'
# result = a()
# print(result)
