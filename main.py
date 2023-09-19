from random import *

# seed(677)

#
# random_float = random()
# print(random_float*random_int)

test_seed = int(input('Create a seed number: '))
seed(test_seed)
random_int = randint(0,1)
print(random_int)
if random_int == 1:
    print('Heads')
else:
    print('Tails')