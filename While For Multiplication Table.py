"""Таблица умножения while for"""

a = 1
while a < 10:
    b = 1
    while b < 10:
        print(('%3d' % (a * b)), end='')
        # print(a,'*',b,'=', a * b)
        b += 1
    print()
    a += 1

for x in range(1, 10):
    for y in range(1, 10):
        print(('%3d' % (x * y)), end='')
        # print(x,'*',y,'=',x*y)
    print()
