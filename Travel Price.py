km = float(input('What is the travel distance in km: \n'))

print('You are about to start a {}km trip'.format(km))
if km <= 200:
    print('Your ticket price will be US${:.2f}'.format(km * 0.50))
else:
    print('Your ticket price will be US${:.2f}'.format(km * 0.45))
