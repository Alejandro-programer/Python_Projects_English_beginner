from random import randint
computer = randint(0, 5)  # 1: The computer thinks of a number.
print('-=-'*20)
print('I will think of a number from 0 to 5. Try to guess it...')
print('-=-'*20)
user_guess = int(input('What number did I think of? \n'))  # 2: The player inputs a number.
print('Processing...')
if user_guess == computer:  # 3: Decides if the player won.
    print('CONGRATULATIONS! You managed to beat me!')
else:
    print('I WON! I beat you, I thought of the number {} and not {}'.format(computer, user_guess))
