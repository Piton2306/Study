"""В какой четверти находится точка"""

from random import randint

x = randint(-10, 10)
y = randint(-10, 10)
print(x)
print(y)
if x > 0 and y > 0:
    print('Первая')
elif x < 0 and y > 0:
    print('Вторая')
elif x < 0 and y < 0:
    print("Третья")
elif x > 0 and y < 0:
    print("Четвертая")
elif x == 0:
    print("Лежит на оси y")
elif y == 0:
    print("Лежит на оси x")
else:
    print()
