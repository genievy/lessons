
#
# #запись в файл (перезаписывает содержимое)
# file = open('readme.txt', 'w')
# file.write('some text')
# file.close()

# #добавление содержимого в файл
# file = open('readme.txt', 'a')
# file.write('\nanother text')
# file.close()

#чтение содержимого для работы с файлом
#метод read
# file = open('readme.txt')
# data = file.read()
# print(data)
# file.close()

# file = open('readme.txt')
# data = file.readlines() #возвращает список строк
# print(data)
# file.close()

# #создаем копию бинарного файла
# pic = 'lenin.jpg'
# file = open(pic, 'rb')
#
# new_file = open('copy ' + pic, 'wb')
# new_file.write(file.read())

#создаем копию  текстового файла
oldtx = 'readme.txt'
r = open(oldtx, 'r')

d = open('copy ' + oldtx, 'w' )
d.write(r.read())


# with open('copy ' + oldtx, 'w') as d:
#     d.write(r.read())
