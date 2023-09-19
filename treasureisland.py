print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print('Welcome to Treasure Island')
print('Your mission is to find the treasure.')
direction = input('Your are at a T-junction, which turn are you going to take Left or Right?\n').lower()
if direction == 'left':
    print("Ouch you've fallen into a bear trap a few steps after making the turn. GAME OVER!")
elif direction == 'right':
    print('''After turning and walking a couple of meters,
    you find yourself at a river bank and you can see a boat
    disappearing off into the horizon''')
    river_choice= input('''You're faced with a choice either to swim to the boat or
     wait for the boat to come back.\nTo swim type Swim\nTo wait type Wait\n''').lower()
    if river_choice == 'swim':
        print('''The river is infested by crocodiles the moment you got into the water,
        two crocodiles pounced on you and ate you. GAME OVER!''')
    elif river_choice == 'wait':
        print('''After hours of waiting the boat finally can back,
        it carried you across the river to an island, on the harbour
        they were three color coded boards.
        To get to the treasure you need to choose the board you'll use
        from the boat
        Red
        Blue
        Yellow''')
        color = input("Which board do you choose?\n").lower()
        if color == 'yellow':
            print('YOU WIN')
        else:
            print('The board broke and you fell into the river and the crocodiles ate you.GAME OVER!!')
    else:
        print('WRONG CHOICE GAME OVER!')
else:
    print('WRONG CHOICE GAME OVER!')
