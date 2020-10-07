def iseven(numb):
    """Определяет чётное или нечётное введённое число"""
    if numb%2 == 0:
        print('Число чётное')
    else:
        print('Число нечётное')
number = int(input('Введите целое число: '))
iseven(number)
