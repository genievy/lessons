

chld = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Borisov_2015']

# srt_chld = sorted(chld)
# print(srt_chld)


def a(child):
    s = child.split('_')[1]
    print(s)
# #
# child = 'Borisov_2015'
# a(child)
# #
#
children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Borisov_2015']
y_list = []

for child in children:
    y_list.append(a(child))

