print('Topic: Dictionary \n')
my_dict = {
    'a':10,
    'b':20,
    'c':30
}
print(my_dict, "\n")
print(type(my_dict), "\n")
print('dictionaries are ordered collections of key-value pairs.')

print('_' * 50)

print('Topic: Check for Duplicates in either keys or values \n')
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'd':10,         # values duplicates are allowed
    'a':20          # key duplicates are not allowed
}
print(my_dict, "\n")

print('_' * 50)

print('Topic: Access a value using a key \n')
print(my_dict['a'], "\n")

print('_' * 50)

print('Topic: Change a Value using a key \n')
my_dict['a'] = 100
print(my_dict, "\n")
print('dictionaries are mutable')

print('_' * 50)

print('Topic: Using Get Method() for a Key not found\n')
user = {
    'name':'John',
    'age':30,
    'city':'New York'
}
print(user.get('country','Unknown' "\n"))    # you should get Unknown if the key is not found. Otherwise, if nothing is specified, it will return None.

print('_' * 50)

print('Topic: Using Membership Operator\n')
print('Is "age" in user?', 'age' in user, "\n")
print('Is "salary" in user?', 'salary' not in user, "\n")

print('_' * 50)

print('Topic: View Dictionary\n')
print(user.keys(), "\n")
print(user.values(), "\n")
print(user.items(), "\n")

print('_' * 50)

print('Topic: Looping through a Dictionary\n')
for key in user:
    print(key,"\n")

print('_' * 50)

print('Topic: Looping through a Dictionary\n')
for key, value in user.items():
    print(key, value, "\n")

print('_' * 50)

print('Topic: Add, Remove, and Update\n')
user['salary'] = 50000
print('Add:', user, "\n")

user.update({'country':'USA', 'salary':60000})
print('Update:', user, "\n")

user.pop('age')
print('Remove:', user, "\n")

user.popitem()
print('Remove last item:', user, "\n")

print('_' * 50)

print('Topic: Using fromkeys method\n')
user = dict.fromkeys(['name','age','city'], 'Unknown')
print(user, "\n")

print('_' * 50)

print('Challenge: Get String Values and Convert to Uppercase \n')
user = {'id':1, 'name':'John', 'age':30, 'city':'New York'}
user_new= {}
for key, value in user.items():
    if isinstance(value, str):
        user_new[key] = value.upper()
    else:
        user_new[key] = value
print('Answer:', user_new, "\n")

new_user = {
    k:v.upper() if isinstance(v, str) else v for k,v in user.items()
}
print('Answer:', new_user, "\n")

