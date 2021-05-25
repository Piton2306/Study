"""Площадь и периметр прямоугольного треугольника"""

import math

a = float(input('Ведите 1 катет = '))
b = float(input('Ведите 2 катет = '))
c = math.sqrt(a ** 2 + b ** 2)
print(c)
s = 0.5 * a * b
p = a + b + c
print('Площадь = %.1f' % s)
print("Периметр = %.1f" % p)
