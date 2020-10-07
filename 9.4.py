L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
print('Начальный список: ', L)
if 'привет' in L:
    L.remove('привет')
else:
    L.append('привет')
print('1. ', L)
print('2. ', L.count(4))
if L.count(4) > 1:
    L.clear()
print(' ', L)
