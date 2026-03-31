print("If-Else independent Exercise: \n")

email = "emmanueleigbedion@gmail.com"
valid = True

# Clean the string
email = email.strip()
print(email, '\n')

# Email must not be empty
if email == "":
    print("Email cannot be empty")
    valid = False

# Email must contain a '.' and "@" symbol
if not("." in email and "@" in email):
    print("Email must contain a . and @")
    valid = False

# Email must contain at least one @ symbol
if email.count("@") != 1:
    print("Email must contain at least one @ symbol")
    valid = False

# Email must end with .com, .net or .org
# if not(email.endswith(".com") or email.endswith(".net") or email.endswith(".org")):   this works too.
if not email.endswith((".com", ".net", ".org")):
    print("Email must end with .com, .net or .org")
    valid = False

# Email must not be longer than 256 characters
if len(email) > 256:
    print("Email must not be longer than 256 characters")
    valid = False

# Email must start aand end with a letter or number
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or number")
    valid = False

if valid:
    print("Email is valid")

print("-"*20)

print("Conditionals (if-elif-else) Challenge: \n")

password = "Eromosele01"
valid=True

# Clean Password
password = password.strip()
print(password, "\n")

# Password must not be empty
if password == "":
    print('Password must not be empty')
    valid = False

# Password must be at least 8 characters
if len(password) <= 8:
    #print(len(password))
    print("Password must be at least 8 characters")
    valid=False

# Passoword must inlude at least one Uppercase
if not any(x.isupper() for x in password):
    print("Password must include at least one Uppercase")
    valid=False

# Password must include at lease one Lowercase
if not any(x.isupper() for x in password):
    print("password must include at least one Lowercase")
    valid=False

# Password must not be the same as the email
if password is email:
    print("password must not be the same as email")
    valid = False

# Password must not contain any spaces
if ' ' in password:
    print("Password must not contain any spaces")
    valid=False

# Password must start and end with a letter or digit
if not(password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")
    valid=False

if valid:
    print("Passoword is valid")

print("_" * 20)

print("Topic: If-Else in One Line \n")

# Note: elif is not allowed in a one-line if-esle statement. Just if and else
score = 100
grade = ("A" if score >= 90 else "F")
print(grade, "\n")

result = 85
mark = ("A" if result >= 90 else "B" if result >= 80 else "F")
print(mark)

print("_" * 20)

print("Topic: Match Case: \n")
country = "United States"
match country:
    case "United States":
        print("US")
    case "Nigeria":
        print("NIG")
    case "England":
        print("ENG")
    case "India":
        print("IN")