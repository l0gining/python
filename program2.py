def arif(a, b, c):
    b = ((a+b+c)/3)
    return b

def printarif(x):
    print('Среднее арифметическое: ', x)

def assign(x):
    sred = x
    return sred

aa = int(input('Введите три числа: '))
bb = int(input())
cc = int(input())
x = arif(aa, bb, cc)
printarif(x)
assign(x)

