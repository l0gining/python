def F1(x):
    a = x**4
    return a

def F2(x):
    a = 4**x
    return a

x = int(input('Введите x: '))
y = int(input('Введите y: '))
aa = F1(x) + F2(x)
bb = F1(y) + F2(x)
print('x^4 + 4^x = ', aa)
print('y^4 + 4^x = ', bb)
