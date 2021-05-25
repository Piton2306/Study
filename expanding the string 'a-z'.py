"""разворачивание строки 'a-z' unicode """


a = 'a'  # the first
b = ""  # the last

while a <= b:
    print(ord(a), end=',')
    a = chr(ord(a) + 1)
