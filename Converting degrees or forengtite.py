"""Перевод в градусы или в форенгейт"""

while True:
    temp = input('Ввветдите температуру C или F = ')
    TEMP = float(temp[:-1])
    if temp[-1] == 'C' or temp[-1] == 'c':
        Tf = 9 / 5 * TEMP + 32
        print('%.1f С = %.1f F' % (TEMP, Tf))
    elif temp[-1] == 'F' or temp[-1] == 'f':
        Tc = 5 / 9 * (TEMP - 32)
        print('%.1f F =%.1f C' % (TEMP, Tc))
    else:
        print('C или F')