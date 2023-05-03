
# посредством метода строки format
# result ='Hello {}'. format(name)
name = 'World'
s = 'Hello {}'
result = s.format(name)
print(result)

# посредством метода строки format
# несколько значений
name1 = 'Oleg'
surname1 = 'Kuznetsov'
s = 'My name is {name} {surname}'
fullname = s.format(name=name1, surname=surname1)
print(fullname)

# посредством f-строки
name = 'World'
result = f'Hello {name}'
print(result)

# посредством f-строки несколько значений
name1 = 'Oleg'
surname1 = 'Kuznetsov'
fullname = f'My name is {name1} {surname1}'
print(fullname)
