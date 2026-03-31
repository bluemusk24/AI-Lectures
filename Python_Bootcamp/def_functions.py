from ast import Not
print("Topic: Args and Kwargs in Functions \n")

def total(*args):
    print(type(args))
    print(sum(args))

# call the function
total = total(1,2,3,4)
print(total, '\n')

print("__" * 20, '\n')

def create_user(**kwargs):
    print(type(kwargs))
    print(kwargs)

# call the function
create_user(
    first_name='Mo',
    last_name='Salah',
    country='Egypt',
    age=33
)

print("__" * 20, '\n')

print("Topic: Return None \n")

def clean(name):
    if not name:
        return None
    else:
        clean_name = name.strip().lower()
        return clean_name

cln = clean("")
print('Output None:', cln)

cleaned = clean(" Emmanuel ")
print('Output Clean Name:', cleaned)

print("__" * 20, '\n')

print("Topic: Return Multiple Outputs \n")

def upper_lower(name):
    lower = name.strip().lower()
    upper = name.strip().upper()
    return lower, upper

low, up = upper_lower(' Eromosele ')
print('lower name:', low)
print('upper name:', up)

print("__" * 20, '\n')

print("Topic: Write to a file \n")

def write_log(message):
    with open('app.log', 'a') as file:
        file.write(message + '\n')

# call function and check created file
write_log('app started')
write_log('user logged in')
write_log('app started')

print("__" * 20, '\n')

print("Topic: Clean Email and Return Structured Data \n")

def clean_and_split(email):
    cln_email = email.strip().lower().split('@')
    return {
        'username':cln_email[0],
        'domain':cln_email[1]
    }

me = clean_and_split(' EMMANUELEIGBEDION@GMAIL.COM ')
print(me)