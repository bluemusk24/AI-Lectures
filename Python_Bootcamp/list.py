print("Topic: How to Create a List \n")
empty = []   # or empty = list()
print("empty list:", empty)  # []
print(type(empty))  # <class 'list'>

print('_' * 50)

letters = ['a', 'b', 'c']
print("letters list:", letters)  # ['a', 'b', 'c']
print(type(letters))  # <class 'list'>

print('_' * 50)

mixed = ["a", 1, 2.0, True, None]
print(type(mixed))  # <class 'list'>
print("Mixed list:", mixed)

print('_' * 50)

alphabets = list("Python")
print("Alphabets list:", alphabets)  # ['P', 'y', 't', 'h', 'o', 'n']

print('_' * 50)

numbers = list(range(5))
print("Numbers list:", numbers)  # [0, 1, 2, 3, 4]

print('_' * 50)

print("Topic: How to Create a Nested List (Matrix) \n")
matrix = [['a', 'b', 'c'],
          [1, 2, 3],
          [True, False, None]]
print("Nested list (matrix):", matrix)  # [['a', 'b', 'c'], [1, 2, 3], [True, False, None]]
print(type(matrix))  # <class 'list'>

print('_' * 50)

print('Topic" How to Access and Read List Elements \n')
print(letters[0])  # 'a'
print(letters[1])  # 'b'
print(letters[-1])  # 'c'

print('_' * 50)

print(matrix[0])  # ['a', 'b', 'c']
print(matrix[0][1])  # 'b'
print(matrix[2][0])  # True
print(matrix[-1][-1])  # None
print(matrix[2][1])  # 2

print('_' * 50)

print('Topic: Slicing Lists \n')
print(letters[:2])  # ['a', 'b']
print(letters[1:])  # ['b', 'c']
print(letters[:])  # ['a', 'b', 'c']

print("_" * 50)

print(matrix[:2])
print(matrix[1:])
print(matrix[0][:2])  # ['a', 'b']
print(matrix[1][1:])  # [2, 3]
print(matrix[2][:])  # [True, False, None]

print('_' * 50)

print('Topic: Python Unpacking Lists \n')

person = ['Alice', 30, 'Engineer', 'New York', 'USA']
name, age, profession, city, country = person
print("Name:", name)  # 'Alice'
print("Age:", age)  # 30
print("Profession:", profession)  # 'Engineer'
print("City:", city)  # 'New York'
print("Country:", country)  # 'USA'

print('_' * 50)

print('Topic: Asterisk (*) Operator in List Unpacking \n')
name, age, *other_info = person
print("Name:", name)  # 'Alice'
print("Age:", age)  # 30   
print("Other Info:", other_info)  # ['Engineer', 'New York', 'USA']

print('_' * 50)

print('Topic: Underscore (_) in List Unpacking \n')   # Underscore removes the item we don't need
name, _, profession, _, country = person
print("Name:", name)  # 'Alice' 
print("Profession:", profession)  # 'Engineer'
print("Country:", country)  # 'USA'

print('_' * 50)

name, *_, country = person
print('name:', name)
print('country:', country)

print('_' * 50)

print('Topic: List Analysis and Exploration \n')
numbers = [10, 20, 30, 40, 50]
print('Max:', max(numbers))  # 50
print('Min:', min(numbers))  # 10
print('Sum:', sum(numbers))  # 150
print('Length:', len(numbers))  # 5
print("All integers:", all(numbers))   # check if all elements in the list are numbers and not zero.  # True
print("Any integers:", any(numbers))   # check if any element in the list is non-zero.  # True
print('All strings:', all(['a', 1, 0, True]))  # False
print('Any strings:', any(['', 0, None, False, 'Hello']))  #
print('Count of 20:', numbers.count(20))  # 1
print('Index of 30:', numbers.index(30))  # 2
print('Find 40:', 40 in numbers)  # True
print('Find 100:', 100 in numbers)  # False
print('No 80 in list:', 80 not in numbers)  # True

print('_' * 50)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [1,2,3]
print("Equal List:",list1==list2)
print("Not Equal List:",list1!=list2)
print("Greater than:",list1>list2)
print("Less than:",list1<list2)
print('Identity:',list1 is list2)
print('Compare list1 and list3:', list1 is list3)
print('Equal List1 and List3:', list1==list3)

print('_' * 50)

print('Topic: Add To List Elements \n')
letters = ['a', 'b', 'c']
letters.append('d')
print("After append:", letters)  # ['a', 'b', 'c', 'd']
letters.insert(1, 'x')
print("After insert:", letters)  # ['a', 'x', 'b', 'c', 'd']
letters.extend(['e', 'f'])
print("After extend:", letters)  # ['a', 'x', 'b', '

print('_' * 50)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix.append([10, 11, 12])
print('Matrix after append:', matrix)
matrix.insert(1, [0, 0, 0])
print('Matrix after insert:', matrix) 
matrix[1].extend('x')
print('Matrix second row after extend:', matrix)

print('_' * 50)

print('Topic: Remove From List Elements \n')
letters = ['a', 'b', 'c', 'd', 'e']
letters.clear()
print("After clear:", letters)  # []
letters = ['a', 'b', 'c', 'd', 'e']
letters.remove('c')
print("After remove 'c':", letters)  # ['a', 'b', '
removed = letters.pop()
print("After pop():", letters)  # ['a', 'b', 'd']
print("Popped element:", removed)  # 'e'
delete = letters.pop(1)
print("After pop(1):", letters)  # ['a', 'd']
print("Popped element at index 1:", delete)  # 'b'

print('_' * 50)

matrix.pop()
print('Matrix after pop():', matrix)
matrix[1].remove(0)
print('Matrix after removing 0 from second row:', matrix)
matrix[-1].pop(2)
print('Matrix after popping index 2 from last row:', matrix)


print('_' * 50)

print('Topic: Update List Elements \n')
letters = ['a', 'b', 'c', 'd']
letters[1] = 'x'   
print("After update index 1 to 'x':", letters)  # ['a', 'x', 'c', 'd']
letters[2:4] = ['y', 'z']  
print("After update slice [2:4] to ['y', 'z']:", letters)  # ['a', 'x', 'y', 'z']

print('_' * 50)

print('Topic: Order List Elements \n')
values = [3, 1, 4, 2]
values.sort()
print("After sort():", values)  # [1, 2, 3, 4]
values.sort(reverse=True)
print("After sort(reverse=True):", values)  # [4, 3,

print('_' * 50)

alpha_matrix = [
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['a', 'b', 'c']
]

alpha_matrix.sort()
print('Matrix after sort():', alpha_matrix)
alpha_matrix.sort(reverse=True)
print('Matrix after sort(reverse=True):', alpha_matrix)

print('_' * 50)

print('Topic: Sorted List Elements \n')     # create a new sorted list without modifying the original list
new_values = sorted(values)
print ("Original values list:", values)  # [4, 3, 2, 1]
print("List After sorted():", new_values)  # [1, 2, 3, 4]

print('_' * 50)

print('Topic: Reverse List Elements \n')
values = [1, 2, 3, 4]
values.reverse()
print("List After Reverse():", values)  # [4, 3, 2, 1]
new_values = list(reversed(values))
print("List After Reversed():", new_values)

print('_' * 50)

print('Topic: Shallow Copy Python Lists \n')
letters = ['a', 'b', 'c']
letters_copy = letters.copy()   # Shallow copy using copy() method
print("Letters Copy using copy():", letters_copy)  # ['a', 'b', 'c']

print('_' * 50)

print('Topic: Deep Copy for Nested List \n')
import copy
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix_deepcopy = copy.deepcopy(matrix)   # Deep copy using copy module
print('Original Matrix:', matrix)
print('Deep Copied Matrix:', matrix_deepcopy)

print('_' * 50)

print('Topic: Lists Combination in Python \n')
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combine_1 = list1 + list2
print("Combined List using + operator:", combine_1, '\n')  # [1, 2, 3, 4, 5, 6]
combine_2 = [list1, list2]
print("Combined List using nesting:", combine_2, '\n')  # [[1, 2, 3], [4, 5, 6]]
list2.extend(list1)
print("Combined List using extend() method:", list2, '\n')  # [1, 2, 3, 4, 5, 6]
combine_3 = list(zip(list1, list2))
print("Combined List using zip() function:", combine_3)  # [(1, 4), (2, 5), (3, 6)]

print('_' * 50)

print('Topic: How to Iterate Through a List \n')
letters = ['a', 'b', 'c']
new_list = []
for letter in letters:
    new_list.append(letter.upper())
    print(new_list)

print('_' * 50)

print('Topic: Enumerate, Reverse, and Zip Functions with Lists \n')
print('Using Enumerate:', list(enumerate(letters)), '\n')  # [(0, 'a'), (1, 'b'), (2, 'c')]. Start can be used to change starting index.
for index, value in enumerate(letters, start=1):
    print(index, value, '\n')
print('Using Reverse:', list(reversed(letters)), '\n')  # ['c', 'b', 'a']
for letter in reversed(letters):
    print(letter, '\n')
numbers = [1, 2, 3]
print('Using Zip:', list(zip(letters, numbers)), '\n')  # [('a', 1), ('b', 2), ('c', 3)]
for letter, number in zip(letters, numbers):
    print(letter, number)

print('_' * 50)

print('Topic: Map with Lists \n')
letters = ['a', 'b', 'c ']
print(list(map(str.upper, letters)), '\n')
numbers = [1, 2, 3, 4]
print(list(map(int, numbers)), '\n')
names = [' Alice ', ' Bob ', ' Charlie ']
print(list(map(str.strip, names)), '\n')
for n in map(str.strip, names):
    print(n)


print('_' * 50)

print('Topic: Filter with Lists \n')
leters = ['a', 'b', 'c', 'd', 'e', None, False, '', 'f']
print('Using Filter with None:', list(filter(None, leters)), '\n')  # ['a', 'b', 'c', 'd', 'e', 'f']
print('Using Filter with bool:', list(filter(bool, leters)), '\n') 
items = ['sql', 'python', '123', '', 'java', '456']
print(list(filter(str.isalpha, items)), '\n')  # ['sql', 'python', 'java']
print(list(filter(str.isnumeric, items)), '\n')  # ['123', '456']
for i in filter(str.isalpha, items):
    print(i)   


# Note: List can be ordered, mutable, indexed, and allow duplicate elements. 