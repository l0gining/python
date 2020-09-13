def arif(a=5, b=4, c=3):
    return ((a+b+c)/3)
print(arif())
x1, x2, x3 = map(int, input('Введите три числа через пробел: ').split( ))
aa = arif(x1, x2, x3)
print(aa)

