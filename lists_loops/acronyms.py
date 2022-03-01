acronyms = ['LOL','IDK','SMH','TBH']

acronyms.append('OMG')
acronyms.remove('SMH')
del acronyms[2]

print(acronyms)

if 'LOL' in acronyms:
    print('True')
else:
    print('False')

for acronym in acronyms:
    print(acronym)

expenses = [142,414,444,11,2,77]

total = sum(expenses)
print(f'You spent ${str(total)} at Gucci today')

total = 0

expenses = []

for i in range(7):
    expenses.append(float(input('Enter an expense:')))

total = sum(expenses)
print(f'You spent ${str(total)} at Gucci today')
