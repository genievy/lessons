

# в основе примера - возможность
# ф-ции print() принимать в качестве
# аргумента открытый для записи файл
# (по умолчанию установлен в вывод на экран)

def print_wrapper(text):
    with open('readme.txt', 'a') as f:
        print(text, file = f)

print_wrapper(1)
