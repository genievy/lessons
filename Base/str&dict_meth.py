
# d = {'Petr': 17, 'Ivan': 22, 'Zina': 19}

def mane_func(b, c, i):
    print(type(b))
    print(dir(b))
    for k in b.keys():
        b[k] = c[i]
        i += 1
    return str(b).center(50, "-")
    # return str(b).ljust(50, "-")
    # return str(b).rjust(50, "-")
b = {}
b = b.fromkeys('Gena')
c = [1, 2, 3, 4]
i = 0
print(mane_func(b, c, i))


# str = "This is the test message"
# result = str.center(50, "-")
# print(result)
#
# str = "+"
# result = ord(str)
# print(result)
# str = result
# result= chr(str)
# print(result)
