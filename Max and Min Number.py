val1 = int(input('First value: '))
val2 = int(input('Second value: '))
val3 = int(input('Third value: '))

smallest = val1
if val2 < smallest:
    smallest = val2
if val3 < smallest:
    smallest = val3

largest = val1
if val2 > largest:
    largest = val2
if val3 > largest:
    largest = val3

print('The smallest value entered was {}'.format(smallest))
print('The largest value entered was {}'.format(largest))
