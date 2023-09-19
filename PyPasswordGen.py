import random
import string
from typing import List, Any

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

#get the size of the string to create
pwd_size = nr_numbers + nr_symbols + nr_letters
# create and array of char[]
#pwd_chars = list(random.choices(letters,weights=None, cum_weights=None, k=pwd_size))
pwd_letters = list(random.choices(letters,weights=None, cum_weights=None, k=nr_letters))
pwd_nums = list(random.choices(numbers,weights=None, cum_weights=None, k=nr_numbers))
pwd_sym = list(random.choices(symbols,weights=None, cum_weights=None, k=nr_symbols))

print(f'The Letters in the pwd: {pwd_letters}\n')
print(f'The numbers in the pwd: {pwd_nums}\n')
print(f'The symbols in the pwd: {pwd_sym}\n')

pwd_chars: list[Any] = pwd_nums+pwd_sym+pwd_letters
random.shuffle(pwd_chars)
print(f'The password chars after shuffle: {pwd_chars}\n')
pwd_c = ""
for p in pwd_chars:
    pwd_c += p

print(f'The password is: {pwd_c}')

