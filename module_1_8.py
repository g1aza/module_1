my_dict = {'Andrey': 1984, 'Anton': 1950, 'Denis': 2002}
print(my_dict)
print(my_dict['Denis'])
my_dict.update({'Valeriy': 2012, 'Nikita': 1998})
my_dict.pop('Anton')
print(my_dict)



my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, True, 'String', (1, 2, 3,)}
print(my_set)
my_set.add('Green')
my_set.add(1.5)
my_set.discard(3)
print(my_set)