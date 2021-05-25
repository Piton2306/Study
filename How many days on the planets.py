"""Сколько земных дней на планетах"""

from math import pi

planet = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
radius = {'Меркурий': 57.91,
          'Венера': 108.25,
          'Земля': 149.6,
          'Марс': 227.95,
          'Юпитер': 778.35,
          'Сатурн': 1425,
          'Уран': 2870,
          'Нептун': 4475}
speed = {'Меркурий': 47.87,
         'Венера': 35.02,
         'Земля': 29.78,
         'Марс': 24.13,
         'Юпитер': 13.07,
         'Сатурн': 9.69,
         'Уран': 6.81,
         'Нептун': 5.43}
for x in range(8):
    t = (2 * pi * radius[planet[x]] * 100000) / speed[planet[x]]
    s = 8640
    if planet[x] == 'Меркурий':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дней')
    elif planet[x] == 'Венера':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дней')
    elif planet[x] == 'Земля':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дней')
    elif planet[x] == 'Марс':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дней')
    elif planet[x] == 'Юпитер':
        print('На планете', planet[x], 'земной год =', round(t / s), 'день')
    elif planet[x] == 'Сатурн':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дня')
    elif planet[x] == 'Уран':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дней')
    elif planet[x] == 'Нептун':
        print('На планете', planet[x], 'земной год =', round(t / s), 'дня')

from math import pi

a = input('Введите планету = ')
radius = {'Меркурий': 57.91,
          'Венера': 108.25,
          'Земля': 149.6,
          'Марс': 227.95,
          'Юпитер': 778.35,
          'Сатурн': 1425,
          'Уран': 2870,
          'Нептун': 4475}
speed = {'Меркурий': 47.87,
         'Венера': 35.02,
         'Земля': 29.78,
         'Марс': 24.13,
         'Юпитер': 13.07,
         'Сатурн': 9.69,
         'Уран': 6.81,
         'Нептун': 5.43}
for x in radius:
    t = (2 * pi * radius[x] * 100000) / speed[x]
    s = 8640
    if x == a:
        print('На планете', a, 'земной год =', round(t / s), 'дней')
        break
    else:
        print('Ошибка')
        break