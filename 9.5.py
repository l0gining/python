import random
List = ['самовар', 'весна', 'лето']
rand_letter = random.choice(random.choice(List))
n = 0
while n != 4:
    answer = input('Введите букву(у вас 4 попытки): ')
    if answer == rand_letter:
        print('Вы угадали!')
        n = 4
    else:
        print('Попробуйте снова!')
        n += 1
        if n == 4:
            print('Вы проиграли :c')
