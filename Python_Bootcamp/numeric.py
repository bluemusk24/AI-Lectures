# Numerical Types
print('Topic: Numerical Types \n')
x = 5
y = 5.7
z = 3 + 4j

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'> 
print(type(z))  # <class 'complex'>

a = "24"
print(int(a))
b = 3.8
print(int(b))
c = 5
print(float(c))
d = 3
e = 4
print(complex(d, e))

print("---" * 20)

# Math Operators
print('Topic: Math Operators \n')
print(5 + 3)    # Addition
print(5 - 3)    # Subtraction
print(5 * 3)    # Multiplication
print(5 / 3)    # Division 
print(5 // 3)   # Get whole number
print(5 % 3)    # Get remainder for odd check
print(4 % 2)    # Get remainder Even check
print(5 ** 3)   # Exponentiation

print("---" * 20)

# Math Shortcuts
print('Topic: Math Shortcuts \n')
x = 5
x += 3  # same as thiis ---> x = x + 3
print(x)
x -= 3  # same as thiis ---> x = x - 3
print(x)
x *= 3  # same as thiis ---> x = x * 3
print(x)    
x /= 3  # same as thiis ---> x = x / 3
print(x)

print("---" * 20)

# Rounding Numbers
print('Topic: Rounding Numbers \n')
price = 35.84950349948393
print(round(price))        # Rounds to nearest whole number
print(round(price, 2))     # Rounds to 2 decimal places
import math
print(math.floor(price))   # Rounds down to nearest whole number
print(math.ceil(price))    # Rounds up to nearest whole number
print(math.trunc(price))   # Removes decimal portion. same as int()

print("---" * 20)

# Absolute Value
print('Topic: Absolute Value \n')
print(abs(-7.25))  # Returns the absolute (positive) value of the specified number

print("---" * 20)

# Random Numbers
print('Topic: Random Numbers \n')
import random
print(random.random())          # Returns a random float number between 0.0 and 1.0
print(random.randint(1, 10))   # Returns a random integer between the two specified numbers (including both)

print("---" * 20)

# Validation: isintegrer() & isintance()
print('Topic: Validation (isinteger & isinstance) \n')
num = 5.0
print(num.is_integer())  # Returns True if the number is an integer, otherwise False
num2 = 5.5
print(num2.is_integer()) # Returns True if the number is an integer, otherwise False

m = 70
print(isinstance(m, int))    # Returns True if the variable is an integer, otherwise False
n = 70.5
print(isinstance(n, int))    # Returns True if the variable is an integer, otherwise False
o = 3 + 5j
print(isinstance(o, complex)) # Returns True if the variable is a complex number, otherwise False


print("---" * 20)

# Practice Exercise: Generate a random integer between 1 and 100, and check if the result is an even number
print('Practice Exercise: \n')
y = random.randint(1, 100)
result = "Even" if y % 2 == 0 else "Odd"
print(f"The number {y} is {result}.")