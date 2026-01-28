salary = float(input('What is your current salary? \n'))

if salary >= 1250:
    new_salary = salary + (salary * 0.10)
else:
    new_salary = salary + (salary * 0.15)

print('Those who earned US${} now earn US${}'.format(salary, new_salary))
