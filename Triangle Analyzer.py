print('\033[33m-=\033[m' * 20)
print('\033[1m Triangle Analyzer\033[m')
print('\033[33m-=\033[m' * 20)

length1 = float(input('First segment: '))
length2 = float(input('Second segment: '))
length3 = float(input('Third segment: '))

print(
    'The segments above CAN FORM a triangle!'
    if length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1
    else 'The segments above CANNOT FORM a triangle!'
)
