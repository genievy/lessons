

# children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Borisov_2015']
# #
# s = []
# for child in children:
#     sername = child.split('_')[0].title()
#     s.append(sername)
#     s.sort()
#
# print(s)

# Сортировка списка по дате рождения.Фамилии с прописной.
#
s = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Borisov_2015']
z = []

# for child in children:
#     sername = child.split('_')[0].title()
#     year = child.split('_')[1]
#     d = [sername, year]
#     s.append(d)
#     def custom_key(people):
#          return people[1]
# s.sort(key = custom_key)
#
# print(d)

for element_old in s:
    a = '_'
    a = a.join(element_old)
    z.append(a)
print(z)

# n = 0
# end = len(children)
#
# def rel(n):
#     sername = children[n].split('_')[0].title()
#     year = children[n].split('_')[1]
#     d = [sername, year]
#     print(d)
#
# for child in children:
#     rel(n)
#     n = n + 1
#     if n <= end
#         continue
