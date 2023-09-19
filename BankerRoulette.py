from random import *

test_seed = int(input('Create a seed number: '))
seed(test_seed)

namesAsCSV = input('Give me everybody\'s names, separated by a comma. ')
names = namesAsCSV.split(', ')
# print(names)
random_int = randint(0,len(names)-1)

print(f'{names[random_int]} is going to buy the meal today!')

print(f'{choice(names)} is going to buy the meal today from the choice method!')