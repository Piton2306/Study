"""Расчитать массу плотность или обём"""

result = None
while True:
    a = input('введите:масса, объем, плотность:')
    if a == 'Масса' or a == 'масса':
        p = float(input('Плотность = '))
        v = float(input('объем = '))
        m = p * v
        print('Масса = %.1f' % (m))
    elif a == 'объем' or a == 'Объем':
        p = float(input('Плотность = '))
        m = float(input('Масса = '))
        v = m / p
        print('Объем = %.1f' % (v))
    elif a == 'Плотность' or a == 'плотность':
        m = float(input('Масса = '))
        v = float(input('объем = '))
        p = m / v
        print('Плотность = %.1f' % (p))
    else:
        print("Ошибка имени")
