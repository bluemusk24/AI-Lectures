print('Topic: Unordered Sets \n')
my_set = {1,2,3,4,5} 
print('my_set:', my_set, "\n")
print(type(my_set), "\n")

print('_' * 50)

print('Topic: Remove Duplicates \n')
set_2 = {2,4,6,2,3,4,6}
print('set_2:', set_2, "\n")

print('_' * 50)

print('Note: Sets are unordered, unindexed, do not allow duplicate values, and are mutable.')

print('_' * 50)

print('Topic: Set Special Methods \n')
a = {10,20,30,40}
a.add(50)
print('add element:', a, "\n")

a.update([60,70,80], 'hello', {90,100})    # just one l prints out bcos sets do not contain duplicates
print('update element:', a, "\n")

a.discard(80)
print('discard element:', a, "\n")

a.remove(70)
print('remove element:', a, "\n")

# Note: discard() does not raise an error if the element is not found, while remove() does raise an error.

print('_' * 50)

print('Topic: Set Math Operations \n')
a = {10,20,30,40}
b = {30,40,50,60}
print('Union of a and b:', a.union(b), "\n")
print(a | b, "\n")  # same as union

print('Intersection of a and b:', a.intersection(b), "\n")
print(a & b, "\n")  # same as intersection

print('Difference of a and b:', a.difference(b), "\n")   # values in a but not in b
print(a - b, "\n")  # same as difference

print('Symmetric Difference of a and b:', a.symmetric_difference(b), "\n")   # values in a or b but not in both
print(a ^ b, "\n")  # same as symmetric difference 

print('Is a a subset of b?', a.issubset(b), "\n")
print('Is b a superset of a?', b.issuperset(a), "\n")

print('_' * 50)

print('Topic: Set Relationship Methods \n')
x = {30,40,50}
y = {30,40,50,60}
print('Is x a subset of y?', x.issubset(y), "\n")
print('Is y a superset of x?', y.issuperset(x), "\n")   
print('Is x a disjoint of y?', x.isdisjoint(y), "\n")


