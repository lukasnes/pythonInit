menus = [
    ['Egg sandwich','Bagle','Coffee'],
    ['BLT','PB&J','Turkey Sandwich'],
    ['Soup','Salad','Spaghetti','Taco']
]

print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

print(menus[0][1])

menus = {
    'Breakfast': ['Egg sandwich','Bagle','Coffee'],
    'Lunch': ['BLT','PB&J','Turkey Sandwich'],
    'Dinner': ['Soup','Salad','Spaghetti','Taco']
}

print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])

for name, menu in menus.items():
    print(f'{name}:\t {menu}')

person = {
    'name': 'Sarah Smith',
    'city': 'Orlando',
    'age': '100'
}
print(f"{person.get('name')} is {person.get('age')} years old")