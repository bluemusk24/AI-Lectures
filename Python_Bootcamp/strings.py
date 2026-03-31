# Strings
print('Topic: Strings \n')
name = "Emmanuel"
print(type(name))

age = 50
print(type(age))
print("Your age is " + str(age) + " years old")

print("---" * 20)

# len built function:
print('Topic: len built function \n')
password = "1234"
print(len(password))

if len(password) < 8:
    print("Short password")

print("---" * 20)

# Count
print('Topic: Count \n')
text = """
Python is easy to learn
Python is popular and powerful
Python is open source
Many people use Python
"""
print("Number of Python words is:", text.count("Python"))

print("---" * 20)

# Transformation
print('Topic: Transformation \n')
price = "123,456"
print(price.replace(",", "."), "\n")
phone = "123-456-789"
print(phone.replace("-", "/"), "\n")
print(phone.replace("-", ""), "\n")
number = '$1,599.99'
print(number.replace("$", "").replace(",", ""))

print("---" * 20)

# Exercise: Convert below number into digits
print('Topic: Practice Exercise \n')
num = "+49 (176) 123-4567"
print(num.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))

print("---" * 20)

# Join(Concatenate) Strings
print('Topic: Strings Concatenation \n')
first_name = "Emmanuel"
last_name = "Eigbedion"
full_name = first_name + " " + last_name
print(full_name)

print("---" * 20)

folder = "C:/Users/Emmanuel/"
file = "test.txt"
path = folder + file
print(path)

print("---" * 20)

# Formatted Strings (f-strings)
print('Topic: Strings Formatting (f-strings) \n')
name = "Emmanuel"
age = 50
is_student = False
print(f"Your name is {name}, your age is {age}, and student status is: {is_student}")

print(f"{{this is me}}")

print("---" * 20)

# Split
print('Topic: Strings Split \n')
stamp = "2026-123-456 14:30:59"
print(stamp.split(" "), "\n")

csv_file = "1234,Emmanuel,Nigeria,Developer,1980-01-01"
print(csv_file.split(","))

print("---" * 20)

# String Repetition
print('Topic: Strings Repetition \n')
print("Hello " * 5, "\n")
print("Na" * 10 + " Batman!", "\n")
print("#" * 20)

print("---" * 20)

# Indexing and Slicing
print('Topic: Strings Indexing and Slicing \n')
name = "Emmanuel"
print(name[0], "\n")  # First character
print(name[-1], "\n")  # Last character
print(name[0:4], "\n")  # First four characters (0 to 3)
print(name[4:], "\n")  # From index 4 to the end
print(name[-3:], "\n")  # Last three characters
print(name[::2], "\n")  # Every second character
print(name[::-1], "\n") # Reverse a string

# Remove whitespaces
print('Topic: Remove Whitespaces \n')
text = "   Engineering"
print(text.strip(),'\n')  # Remove left whitespaces
docs = "Documents   "
print(docs.strip(),'\n')  # Remove right whitespaces
data = "   Data Science   "
print(data.strip(),'\n')  # Remove both left and right whitespaces
message = "###Hello World###"
print(message.strip("#"),'\n')  # Remove specific characters from both ends

print(len(text), len(text.strip()))
print(len(text) - len(text.strip()), "whitespaces removed")
print(len(text) == len(text.strip()))

print("---" * 20)

# Case Conversion
print('Topic: Case Conversion \n')
course = "python for Beginners"
print(course.upper(),'\n')  # Uppercase
print(course.lower(),'\n')  # Lowercase
print(course.title(),'\n')  # Title Case

search = "Email "
data = " emAil"
print(search == data, "\n")
print(search.strip().lower() == data.strip().lower(), "\n")

# Exercise: Clean the following data
print('Topic: Practice Exercise \n')
data = "968-Maria, (D@t@ Engineer);; 27y "
print(data.replace("968-", "name: ").replace(", (", " | role: "). replace("@", "a").replace(";;" , " | age: ").lower().replace(')', ""))

print("---" * 20)

# Search: True or False
print('Topic: Search - True or False \n')
data = "2025-October-26"
print(data.startswith("2025"), "\n")
print(data.endswith("26"), "\n")
print(data.startswith("25", 5, 12), "\n")  # Check if
print("Feb" in data, "\n") # check if Feb is in data
print("Oct" in data, "\n") # check if Oct is in data
print(data.find("October"), "\n")     # print the starting index of October = 5
print(data.find("2023"), "\n")        # -1 means not found

phone = "+1(806-300-5084)"
print(phone.startswith("806"), "\n") # Check if phone starts with 806
print(phone.find("806") > -1, "\n") # Check if 806 is in phone and greater than -1

phone1 = "+48-176-12345"
phone2 = "48-168-15342"
phone3 = "0048-170-14325"

print(phone1[phone1.find("-") + 1:])
print(phone2[phone2.find("-") + 1:])
print(phone3[phone3.find("-") + 1:])

print("---" * 20)

# Validations
print('Topic: Validations \n')
country = "Nigeria"
print(country.isalpha())  # Check if all characters are alphabets
digit = "123456"
print(digit.isnumeric())  # Check if all characters are digits
nation = "USA1"
print(nation.isalpha())