my_name = ('Salekh', 'Mamadaliev', 19)
people = []
people.append(my_name)
friend_1 = ('Paul', 'Green', 22)
friend_2 = ('Mary', 'Adamson', 18)
friend_3 = ('Betty', 'Fisher', 19)
people.append(friend_1)
people.append(friend_2)
people.append(friend_3)
print('Несортированный список:')
print(people)
print('Сортировка по имени:')
people.sort(key = lambda x: x[0])
print(people)
print('Сортировка по фамилии:')
people.sort(key = lambda x: x[1])
print(people)
print('Сортировка по возрасту:')
people.sort(key = lambda x: x[2])
print(people)
