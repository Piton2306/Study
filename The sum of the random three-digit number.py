"""Сумма случайного трёхзначного числа"""

from random import randint

a = randint(100, 1000)
print(a)
s = a // 100  # сотые
print(s)
d = a // 10 % 10  # десятые
print(d)
o = a % 10  # остаток
print(o)
print(s + d + o)
