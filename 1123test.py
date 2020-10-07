def Fair (a):
    b = 9/5 * a + 32
    return b

def area(a):
    b = a**2
    c = a*4
    return b, c

def arif(a, b, c):
    b = ((a+b+c)/3)
    return b

TC = int(input('Введите градусы цельсия: '))
TF = Fair (TC)
print('Градусы Фаренгейт: ', TF)

a = int(input('Введите сторону квадрата: '))
Area = area(a)
S, P = area(a)
print('Площадь квадарата со стороной ', a, ' равна ', S, '.', ' Периметр квадрата со стороной ', a, ' равен ', P)

aa = int(input('Введите три числа: '))
bb = int(input())
cc = int(input())
brif = arif(aa, bb, cc)
print('Среднее арифметическое равно: ', brif)
