print('Welcome to the Love Calculator!')
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')

master_word1 = 'TRUE'
master_word2 = 'LOVE'
search_word = name1.upper() + name2.upper()
# print(f'search couple name in upper case: {search_word}')
true_counter = 0
for i in search_word:
    for x in master_word1:
        if i == x:
            true_counter += 1
            # print(f'value for x:{x} & i:{i} and count is:{true_counter}')

love_counter = 0
for i in search_word:
    for x in master_word2:
        if i == x:
            love_counter += 1
            # print(f'value for x:{x} & i:{i} and count is:{love_counter}')

love_score = int(str(true_counter)+str(love_counter))

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 <= love_score <= 50:
    print(f'Your  score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}')







