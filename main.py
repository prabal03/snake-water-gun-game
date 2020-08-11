print('%50s' % 'Snake Water Gun Game')
print('Rule:\n1.Snake vs Water: Snake wins\n2.snake vs Gun: Gun wins\n3.Water vs Gun: Water wins')
from random import choice


def main():
    # r is the points of computer
    r = 0
    # u is the points of user
    u = 0
    # c is no of chances
    c = 4

    for i in range(c):
        randomly = choice(['Snake', 'Water', 'Gun'])
        user = input('\nenter the choices from the following\ns for snake\nw for water\ng for gun\ninput='.lower())
        if randomly == 'Snake' and user == 's':
            print(f'\nmatch is draw. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Snake' and user == 'w':
            r = r + 1
            print(f'\ncomputer won. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Snake' and user == 'g':
            u = u + 1
            print(f'\nyou won. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Water' and user == 'w':
            print(f'\nmatch is draw. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Water' and user == 's':
            u = u + 1
            print(f'\nyou won. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Water' and user == 'g':
            r = r + 1
            print(f'\ncomputer won. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Gun' and user == 'g':
            print(f'\nmatch is draw. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Gun' and user == 's':
            r = r + 1
            print(f'\ncomputer won. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        elif randomly == 'Gun' and user == 'w':
            u = u + 1
            print(f'\nyou won. computer point is: {r} and your point is: {u} ')
            c = c - 1
            print('no of chances left', c)
        else:
            print('\npllzz give correct input!!')

    if r > u:
        print('\nComputer is the winner!!!!')
    elif r == u:
        print(' \nMatch Draw!!!!')
    else:
        print('\nCongratulations you won the game!!!!')


main()
s = input('\n\ndo you want to run again\npress y for yes or n for no=')
if s == 'y':
    main()
else:
    print('\nGAME IS OVER!!')
