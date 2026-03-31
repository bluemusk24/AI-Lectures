print('Topic: Lambda Functions in Python \n')
multiply = lambda x: x*2
print(multiply(2))
add = lambda x, y: x + y
print(add(3, 5))
check = lambda s: s in 'Python'
print(check('P'))
print(check('Z'))

print('_'* 40)

print('Topic: Using Lambda Functions with Map() \n')
prices = ['$5.30', '$4.20', '$6.30', '$7.80']
print('Map each element to Float:', list(map(lambda x: float(x.replace('$', '')), prices)))


print('_'* 40)

print('Topic: Using Lambda Functions with Filter() \n')
values = [100, 200, 50, 75, 300, 25]
print('Filter row >= 1000:', list(filter(lambda x: x >= 100, values)), '\n')  # [100, 200, 300]
students = [['Emman', 85], ['John', 65], 
            ['Doe', 90], ['Jane', 55]]
print('Filter row > 70:', list(filter(lambda row: row[1] >= 70, students)), '\n')  # [['Emman', 85], ['Doe', 90]]
print('First Character startswith E:', list(filter(lambda name: name[0].startswith('E'), students)), '\n')  # [['Emman', 85]]

print('_'* 40)

print('Topic: Using Lambda Functions with Sorted() \n')
numbers = [4, 2, 9, 1, 5, 6]
print('Sorted Ascending:', sorted(numbers))  # [1, 2, 5, 5, 6, 9]
print('Sorted Descending:', sorted(numbers, reverse=True))  # [9, 6
print('Sorted with Lambda (Ascending):', sorted(numbers, key=lambda x: x))  # [1, 2, 4, 5, 5, 6, 9]
print('Sorted with Lambda (Descending):', sorted(numbers, key=lambda x: x, reverse=True))  # [9, 6, 5, 5, 4, 2, 1]