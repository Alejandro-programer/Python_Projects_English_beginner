name = str(input('Enter your full name: \n')).strip().upper()

print('The letter A appears {} times'.format(name.count('A')))
print('The first letter A appeared at position {}'.format(name.find('A') + 1))
print('The last letter A appeared at position {}'.format(name.rfind('A') + 1))
