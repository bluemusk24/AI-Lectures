print('Topic: Creating Tuples \n')
my_tuples = (10,20,30, 5)

print(my_tuples, "\n")

print(type(my_tuples), "\n")

print(my_tuples[0], "\n")

print(my_tuples[-1], "\n")

print("Sorted Tuple: ", sorted(my_tuples))   # this gave an ordered list because tuple is immutable

print("Count of 10: ", my_tuples.count(10), "\n")

print("Index of 20: ", my_tuples.index(20), "\n")

print("Length of Tuple: ", len(my_tuples), "\n")

print("Max of Tuple: ", max(my_tuples), "\n")

print("Min of Tuple: ", min(my_tuples), "\n")

print("Sum of Tuple: ", sum(my_tuples), "\n")


# Note: Tuples are ordered, indexed, allow duplicate values, and are immutable