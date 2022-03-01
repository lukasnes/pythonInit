acronyms = {'LOL':'laugh out loud', 'IDK':"I don't know"}
menu = {'Soup': 5, 'Salad': 6}

acronyms['TBH'] = 'to be honest'
print(acronyms)

# definition = acronyms['BTW'] will return a keyerror.
# Instead:

definition = acronyms.get('BTW')
if definition:
    print(definition)
else:
    print("Key doesn't exist.")

# Using .get will not return an error if the item does not exist.

sentence = 'IDK what happened TBH'
translation = f"{acronyms.get('IDK')} what happened {acronyms.get('TBH')}"

print('sentence:', sentence)
print('translation:', translation)