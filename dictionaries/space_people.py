import requests

response = requests.get('http://api.open-notify.org/astros.json')
response_json = response.json()

number = response_json.get('number')
people = response_json.get('people')

print(f'The number of people currently in space is {number}')
for key in people:
    print(f"{key['name']} is aboard the {key['craft']}")
