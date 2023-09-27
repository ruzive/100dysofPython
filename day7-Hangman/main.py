import random
import hangmanArt as handman

word_list = ['children', 'ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
d_guess = []
for n in chosen_word:
        d_guess.append("_")

print(d_guess)
print(len(handman.hangman))

# print(chosen_word)
lives = 8
ind = 0
has = d_guess.__contains__("_")
while has and lives != 0:
    guess = input('Guess a letter:\n').lower()
    v = 0
    print(f'hangman list size - lives is: {len(handman.hangman)} - {lives} = {len(handman.hangman) - lives}')
    if guess not in chosen_word:
        print(handman.hangman[len(handman.hangman) - lives])
        lives -= 1
        ind +=1
    else:
        for i in chosen_word:
            if i == guess:
                # d_guess.pop(v)
                # d_guess.insert(v, i)
                d_guess[v]= i
            v += 1
        has = d_guess.__contains__("_")
        print(d_guess)

if not has:
    print("you win")
elif lives == 0:
    print('you lose')

