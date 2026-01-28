speed = int(input('What is the current car speed? \n'))

if speed <= 80:
    print('Have a nice day! Drive safely!')
else:
    print('FINED! You exceeded the limit of 80km/h')
    print('You must pay a fine of US${:.2f}'.format((speed - 80) * 7))
    print('Have a nice day! Drive safely!')
