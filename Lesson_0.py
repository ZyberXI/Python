#1) Создать переменную типа String
#2) Создать переменную типа Integer
#3) Создать переменную типа Float
#4) Создать переменную типа Bytes
#5) Создать переменную типа List
#6) Создать переменную типа Tuple
#7) Создать переменную типа Set
#8. Создать переменную типа Frozen set
#9) Создать переменную типа Dict

a = str('Hello world')
print(a, type(a))

b = int(123)
print(b, type(b))

c = float(123)
print(c, type(c))

d = bytes(2)
print(d, type(d))

e = list('hello world')
print(e, type(e))

f = tuple('hello world')
print(f, type(f))

g = set('hello world')
print(g, type(g))

h = frozenset('hello world')
print(h, type(h))

i = dict(first='hello', second='world')
print(i, type(i))


#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(a, type(a), b, type(b), c, type(c), d, type(d), e, type(e), f, type(f), g, type(g), h, type(h), i, type(i),)

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
x = 'From Russia'
y = 'With Love'
print(x,y)
print(x+' '+y)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

x1 = 15
x2 = 'rabbits'

print(x1,x2)
print(str(x1)+' '+x2)



