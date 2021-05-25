"""Угадай случайное число число"""
import random

b = -1
a = random.randint(0, 10)
print(a)
proverka = 0
while b != a:
    b = int(input("Угадай число = "))
    if b < a:
        print(b, '= Слишком мало')
        proverka += 1
    elif b==a:
        print(b, '= молодец')
    else:
        print(b, "= Слишком много")