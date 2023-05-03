
#start: указывает начало значения индекса.
#Это необязательно, по умолчанию – None

#stop: указывает конец значения индекса.
#Это обязательный параметр.

#step: указывает шаги,
#которые нужно выполнить от начала до остановки index.
#Это необязательный параметр, значение по умолчанию – None.

wr = 'HelloWorld'
s = slice(1, 10, 2) # indexes 1,3,5,7,9
print(type(s))
print(s.start)
print(s.stop)
print(s.step)
print(wr[s])

print()

s = slice(5) # indexes 0,1,2,3,4
print(type(s))
print(s.start)
print(s.stop)
print(s.step)
print(wr[s])
