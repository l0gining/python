def summ(a, b, c):
    return a+b+c

def mul(a, b, c):
    return a*b*c

A = int(input('Введите первое число: '))
B = float(input('Введите второе число: '))
C = int(input('Введите третье число: '))
print('Сумма введенных чисел: ', summ(A, B, C))
print('Произведение введенных чисел', mul(A, B, C))
