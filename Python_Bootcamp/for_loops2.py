print("Topic: Break Statement for Loops \n")
names = ["Alice", "Bob", "Charlie", "", "David"]
for name in names:
    if name == "":
        print("Empty name found, stopping the loop.") # not compulsory to print
        break
    print(f"Hello, {name}!")

print("__" * 20)

print("Topic: Continue Statement for Loops \n")
for name in names:
    if name == "":
        print("Empty name found, skipping to the next iteration.") # not compulsory to print
        continue
    print(f"Hello, {name}!")

print("__" * 20)

print("Topic: Pass Statement for Loops \n")
for name in names:
    if name == "":
        #pass  # Placeholder for future code
        name = name.replace("", "No Name")  # Example action
        print("Empty name found, replacing with 'No Name'.") # not compulsory to print
    else:
        print(f"Hello, {name}!")

print("__" * 20)

print("Challenge: Using Break, Continue, and Pass \n")
# Skip the weekend day
days = ["Mon", "Sun", "Tue", "Wed", "Sat", "Thu", "Fri"]
weekends = ["Sun", "Sat"]
for day in days:
    if day in weekends:
        continue
    print(f"Working on {day}")

print("__" * 20)

print("Challenge_2: Break \n")
emails = ["data@gmail.com", "bush@yahoomal.com", "Datat hahcker;", "maria@hotmail.com"]
for email in emails:
    if ';' in email:
        print(f"Invalid email found: {email}, stopping the process.")
        break
    print(f"Processing email: {email}")

print("__" * 20)

print("Else Statement with For Loops \n")   # Else works with for loop if Python iterates through the whole sequence and combines with break statement.
items = [10, 20, 35, 40]
for i in items:
    if i % 2 != 0:
        print("Odd number found:", i)
        break
else:
    print("All numbers are even.")

print("__" * 20)

items = [10, 20, 30, 40]
for i in items:
    if i % 2 != 0:
        print("Odd number found:", i)
        break
else:
    print("All numbers are even.")

print("__" * 20)

print("Check for csv files \n")
files = ["data.csv", "report.txt", "summary.csv"]
for file in files:
    if not file.endswith('.csv'):
        print("Non-csv file found:", file)
        break
else:
    print("All files are csv files.")

print("__" * 20)

files = ["data.csv", "report.csv", "summary.csv"]
for file in files:
    if not file.endswith('.csv'):
        print("Non-csv file found:", file)
        break
else:
    print("All files are csv files.")


print("__" * 20)

print("Challenge: Duplicate files Checker \n")
file_list = ["data.csv", "report.txt", "summary.csv", "data.csv"]
seen_files = set() 
for file in file_list:
    if file in seen_files:
        print("Duplicate file found:", file)
        break
    seen_files.add(file)
else:
    print("No duplicate files found.")

