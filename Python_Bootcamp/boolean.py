# Boolean values in Python to see if there is a value or not
print(('Boolean Checks: \n'))
print(bool(123))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool(0))
print(bool("Hello"))

print("---" * 20)

# Any and All
print('Topic: Any and All \n')
email = ""
phone = "1234567890"
username = "Emmanuel"
print(any([email, phone, username]))  # True if any value is True else False
print(all([email, phone, username]))  # True if all values are True else False

print("---" * 20)

# Isinstance
print('Topic: Isinstance \n')
print(isinstance(123, int))  # Check if value is of a certain type
print(isinstance("Hello", str))
print(isinstance(12.5, bool))

print("---" * 20)

# Comparison Operators
print('Topic: Comparison Operators \n') 
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)
print(3 == 2)
print(3 != 2)
print("abc" > "ab")
print("abc" > "abcd")  
print("abc" > "ABC")
print("abc" >= "ABC")
print(1 < 2 < 3 )
print(1 < 3 > 2 )
print(1 < 3 == 3 )

print("---" * 20)

# Logical Operators: and, or, not   
print('Topic: Logical Operators \n')
print(3 > 2 and 2 > 1)  # True if both conditions are True
print(3 > 2 and 2 < 1)  # False if any one condition is False
print(3 > 2 or 2 < 1)   # True if any one
print(not(3 > 2))       # Negates the condition, False becomes True and True becomes False
cpu_usage = 90
memory_usage = 70
print(cpu_usage > 80 and memory_usage > 80)  # True if both conditions are True
print(cpu_usage > 80 or memory_usage > 80)   # True if any one

name = ""
print(bool(name))
print(not name)  # True if name is empty

print("---" * 20)

# Practice Problems
print('Topic: Practice Problems \n')

# 1. Check if a user's name is not empty and the age is greater than or equal to 18
import random
is_username = False
user_age =  random.randint(15, 20)
print(f'User age: {user_age}')
print(not is_username and user_age >= 18, "\n")

# 2. Check if the password is at least 8 characters long and does not contain spaces
password = "mypassword"
print(len(password) >= 8 and " " not in password, "\n")

# 3. Check if a user's email is not empty, contains "@" and ends with '.com'
email = 'emmanueleigbedion@gmail.com'
print(bool(email) and (email.find('@') and email.endswith('.com')), "\n")

# 4. Check if a username is a string, is not None and is greater than 5 characters
username = "Emmanuel"
print(isinstance(username, str) and username is not None and len(username) > 5, "\n")

# 5. Check if the user is either an admin or a moderator, and either they are not banned or they have verified their email
is_admin = True
is_moderator = False
is_banned = False
is_email_verified = True
print((is_admin or is_moderator) and (not is_banned or is_email_verified))

print("---" * 20)

# Membership (in, not in) Operators:
print('Topic: Membership and Identity Operators \n')
print("f" not in "Python")  # True if 'f' is not found in the string
print(3 in [1,2,3,4])    # True if 3 is found in the list
print(5 not in (1,2,3,4)) # True if 5 is not found in the tuple
print("name" in {"name": "Emmanuel", "age": 25})  # True if 'name' is found in the dictionary keys

print("---" * 20)

# Identity (is, is not) Operators:
print('Topic: Identity Operators \n')
a = [1, 2, 3]
b = a
print(a is b)       # True if both variables point to the same object
print(a is not b)   # False if both variables point to the same object
c = [1, 2, 3]  
print(a is c)       # False because they are different objects even though they have the same content
print(a == c)       # True because they have the same content
m=5
n=5
print(m is n)       # True because both point to the same object in memory
print(m is not n)   # False because both point to the same object in memory 
print(m == n)       # True because they have the same value